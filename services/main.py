import os
from dataclasses import dataclass
from service import Service
from box import Box
import json

@dataclass
class IndividualService:
    name: str
    config_path: str

    def create_service(self) -> Service:
        return Service(self.config_path)


class ServiceManager:
    def __init__(self, config_dir="services/configs"):
        self.services = {}
        self._load_services_from_configs(config_dir)

    def _load_services_from_configs(self, config_dir):
        for config_file in os.listdir(config_dir):
            if config_file.endswith(".json"):
                service_name = config_file.split(".")[0]
                config_path = os.path.join(config_dir, config_file)
                with open(config_path, 'r') as f:
                    config = Box(json.load(f))
                self.services[service_name] = IndividualService(name=service_name,
                                                                config_path=config_path)

    def list_services(self):
        # ! change to id and name
        for service_name in self.services:
            print(service_name)

    def get_service_by_name(self, name):
        # ! change to select by id
        if service := self.services.get(name):
            return service.create_service()
        print(f"Service '{name}' not found.")
        return None

    def select_service(self):
        self.list_services()
        choice = input("Choose a service by entering its name: ")
        return self.get_service_by_name(choice)


# Example usage:
if __name__ == "__main__":
    manager = ServiceManager()

    if selected_service := manager.select_service():

        # selected_service.create_account(email="d.skoliba@mcdomaine.fr.nf")

        selected_service.register(
            url = "https://wolt.com/me/magic_login?email=d---%40mcdomaine.fr.nf&email_hash=-bv_g4ArsjZrg19HyKPcGDwoOiLgKQPty2BpprVvIi8&token=yLNgFYamjVb7aWci4JmTzIyoz0jZMaitGujCwd7Ji9g&new_user=true&attribution=GA1.1.995373538.1696372643%3A75f05196-8c51-4fe0-a9ae-308cb9d4f010%3A",
            country = "POL",
            first_name = "Jan",
            last_name = "paweldrugi",
            country_code = "PL",
            phone_number = "123456789",
            referral_code = "",
        )

        # enter sms code
        # ! todo -> wolt.json
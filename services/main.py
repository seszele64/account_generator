from .service import Service, Actions
from .enums import Services

class ServiceManager:
    def __init__(self):
        self.services = {}

    def add_service(self, service):
        self.services[service.name] = service

    def select_service(self, service_name):
        self.selected_service = self.services[service_name]

    def execute_selected_service(self, **kwargs):
        self.selected_service.execute(**kwargs)

def main(**kwargs):
    manager = ServiceManager()

    # select service 
    manager.select_service(Services.WOLT)

    # select action -> load from Service class 
    manager.selected_service.select_action()

    # select action -> print all actions
    manager.selected_service.print_actions()

    # execute action
    manager.selected_service.execute(
        # verification / mail / links
        url = "https://wolt.com/me/magic_login?email=d---%40mcdomaine.fr.nf&email_hash=-bv_g4ArsjZrg19HyKPcGDwoOiLgKQPty2BpprVvIi8&token=yLNgFYamjVb7aWci4JmTzIyoz0jZMaitGujCwd7Ji9g&new_user=true&attribution=GA1.1.995373538.1696372643%3A75f05196-8c51-4fe0-a9ae-308cb9d4f010%3A",
        # real_data
        country = "POL",
        # fake data
        first_name = "Jan",
        last_name = "paweldrugi",
        # real_data
        country_code = "PL",
        # phone number to be taken from verification service
        phone_number = "123456789",
        referral_code = "",
    )



    # if selected_service := manager.select_service():

    #     # select action
    #     action = selected_service.select_action()

    #     selected_service.execute(
    #         # verification / mail / links
    #         url = "https://wolt.com/me/magic_login?email=d---%40mcdomaine.fr.nf&email_hash=-bv_g4ArsjZrg19HyKPcGDwoOiLgKQPty2BpprVvIi8&token=yLNgFYamjVb7aWci4JmTzIyoz0jZMaitGujCwd7Ji9g&new_user=true&attribution=GA1.1.995373538.1696372643%3A75f05196-8c51-4fe0-a9ae-308cb9d4f010%3A",
    #         # real_data
    #         country = "POL",
    #         # fake data
    #         first_name = "Jan",
    #         last_name = "paweldrugi",
    #         # real_data
    #         country_code = "PL",
    #         # phone number to be taken from verification service
    #         phone_number = "123456789",
    #         referral_code = "",
    #     )

    #     # enter sms code
    #     # ! todo -> wolt.json



# # Example usage:
# if __name__ == "__main__":

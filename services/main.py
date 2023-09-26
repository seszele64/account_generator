import wolt


class Service:
    create_account = None
    register = None
    login = None

SERVICES = {
    'wolt': wolt
}


# let user insert values
# ! use custom datatype to hold values
def insert_user_values(
    service_name: str,
    **kwargs
):
    # index SERVICE[service_name] -> get service object
    custom_service = SERVICES[service_name]

    # service is a module
    def insert_user_values(method: str,
                           **kwargs):
        
        registration_response = None

        if hasattr(custom_service, method):
            registration_response = custom_service.create_account(**kwargs)
            return registration_response
        
        else:
            raise NotImplementedError(
                f"Method {method} not implemented for service {service_name}"
            )
    
    return insert_user_values(service=custom_service, **kwargs)

# use: insert_user_values(service_name="wolt", method="create_account", **kwargs)
class WoltData(Service):

    def __init__(self, **kwargs):
        self.create_account = insert_user_values(service_name="wolt", method="create_account", **kwargs)
        self.register = insert_user_values(service_name="wolt", method="register", **kwargs)
        self.login = insert_user_values(service_name="wolt", method="login", **kwargs)
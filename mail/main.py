from yopmail import Yopmail
from links import *

# check link in mail
# link = check_link_inbox('twoja.mama@mymailbox.xxl.st', 'wolt')

def create_mail_address(
    name: str,
    surname: str,
    domain: str = 'yopmail.com'
) -> str:
    return f"{name}.{surname}@{domain}"


# look for link in mail
def check_link_inbox(
    mail_address: str,
    service_name: str,
    type: str = 'verification'
):
    
    """
    Checks the inbox of the specified `mail_address` for a link of the given `type` related to the `service_name`.

    Args:
        mail_address (str): The email address to check the inbox for.
        service_name (str): The name of the service to retrieve the link from.
        type (str, optional): The type of link to retrieve. Defaults to 'verification'.

    Returns:
        str: The link found in the inbox, or None if no link is found.

    Example:
        ```python
        mail_address = "example@example.com"
        service_name = "example_service"
        link = check_link_inbox(mail_address, service_name, type='verification')
        if link:
            print(f"Verification link found: {link}")
        else:
            print("No verification link found.")
        ```
    """

    yopmail = Yopmail(mail_address)
    service = ServiceRegistry.get_service(service_name)

    def mail_check(
            mail: object,
            type: str = 'verification'
    ):
        
        if type == 'verification':
            return service.get_verification_link(mail)
        elif type == 'password':
            return service.get_password_reset_link(mail)
    
    # iterate over all mails starting from last one until we find link
    all_mails = yopmail.get_mail_ids()

    for mail_id in all_mails:
        mail = yopmail.get_mail_body(mail_id)
        if (link := mail_check(mail)):
            return link
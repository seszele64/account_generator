from yopmail import YopmailManager
from links import (get_link_from_mail)

def create_mail_addres(
    name: str = None,
    surname: str = None
) -> str:
    """
    Creates a mail address for the given `name` using the Yopmail domain.

    Args:
        name (str): The name to create the mail address for.
        surname (str): The surname to create the mail address for.

    Returns:
        str: The mail address created for the given `name`.

    Example:
        ```python
        mail_address = create_mail_addres(name='John', surname='Doe')
        print(mail_address)
        ```
    """
    def format_name(name: str) -> str:
        """
        Formats a name by removing special characters and converting to lowercase.

        Args:
            name (str): The name to format.

        Returns:
            str: The formatted name.
        """
        import re
        return re.sub('[^A-Za-z0-9]+', '', name).lower()
    
    name = format_name(name)
    surname = format_name(surname)

    return f"{name}.{surname}{YopmailManager().get_todays_domain()}"

def check_link_inbox(
    username: str,
    service_name: str,
    type: str = 'verification'
):
    """
    Checks the inbox of the specified `username` for a link of the given `type` related to the `service_name`.

    Args:
        username (str): The username of the mail address to check.
        service_name (str): The name of the service to retrieve the link from.
        type (str, optional): The type of link to retrieve. Defaults to 'verification'.

    Returns:
        str: The link found in the inbox, or None if no link is found.

    Example:
        ```python
        link = check_link_inbox(username='example', service_name='example_service', type='verification')
        if link:
            print(f"Verification link found: {link}")
        else:
            print("No verification link found.")
        ```
    """
    mail_manager = YopmailManager()

    if (mail := mail_manager.get_newest_mail_for_username(username)):
        return get_link_from_mail(service_name, mail.html, type=type)
    else:
        return None
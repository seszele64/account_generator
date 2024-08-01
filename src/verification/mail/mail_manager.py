from .yopmail import YopmailManager
from .links import MailLinkExtractor

class MailManager:

    def __init__(self):
        self.yopmail_manager = YopmailManager()

    def create_mail_address(
        self,
        username: str,
    ) -> str:
        
        """
        Creates a mail address for the given `name` using the Yopmail domain.

        Args:
            name (str): The name to create the mail address for.

        Returns:
            str: The mail address created for the given `name`.

        Example:
            ```python
            mail_address = create_mail_addres(name='John')
            print(mail_address)
            ```
        """
        name = self.format_name(username)
        return f"{name}{self.yopmail_manager.get_todays_domain()}"

    def check_link_inbox(
        self,
        regex_pattern: 're.Pattern',
        username: str,
    ):
        """
        Checks the inbox of the specified `username` for a link of the given `type` related to the specified `service`.

        Args:
            username (str): The username of the mail address to check.
            regex_pattern (re.Pattern): The regex pattern to use to find the link.

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
        if (mail := self.yopmail_manager.get_newest_mail_for_username(username)):
            return MailLinkExtractor(mail).extract_link(regex_pattern)
        else:
            return None

    def get_verification_link_for_username(self, username, regex_pattern: 're.Pattern') -> str | None:
        if (mail := self.yopmail_manager.get_newest_mail_for_username(username)):
            return MailLinkExtractor(mail).extract_link(regex_pattern)
        else:
            return None

    def format_name(self, name: str) -> str:
        """
        Formats a name by removing special characters and converting to lowercase.

        Args:
            name (str): The name to format.

        Returns:
            str: The formatted name.
        """
        import re
        return re.sub('[^A-Za-z0-9.]+', '', name).lower()


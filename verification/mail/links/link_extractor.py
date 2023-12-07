import re
# Import your regex classes
from .enums import *


class MailLinkExtractor:
    """
    A class representing a mail link extractor.
    """

    ServiceLinks = ServiceLinksEnum

    def __init__(self, email_content: str):
        self.email_content = email_content
    
    def extract_links(self, pattern_enum: re.Pattern) -> list:
        """
        Extracts the links from the email content using the given regex pattern.
        """
        return re.findall(pattern_enum,
                          self.email_content.html)
    
    def extract_link(self, pattern_enum: re.Pattern) -> str:
        """
        Extracts the link from the email content using the given regex pattern.
        """
        found_links = self.extract_links(pattern_enum)
        return found_links[0] if found_links else None
    



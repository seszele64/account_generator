import re
# Import your regex classes
from .registry import regex_registry
from .services import register_services

# Register your regex patterns
register_services()

def get_link_from_mail(service_name: str, email_content: str, type: str = 'verification') -> str:
    """
    Retrieve the link from the email content.
    """
    # Use RegexRegistry to get necessary regex pattern
    regex_pattern = regex_registry.query(service_name, type)

    # Use regex to find the link
    link = re.search(regex_pattern, email_content)

    # Return the link
    return link.group(0) if link else None
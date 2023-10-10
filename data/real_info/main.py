# create user agent
from .user_agent import UserAgent
from .password import get_random_string as get_random_password

# create random user agent on each call
def get_random_user_agent():
    return UserAgent().get_random_user_agent()

# create random user agent
random_user_agent = get_random_user_agent()
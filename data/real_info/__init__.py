# imports
from real_info import (
    UserAgent,
    get_user_agent,
    app,
    shutdown_requested,
)

# read user agent from file
user_agent = UserAgent.get_user_agent()
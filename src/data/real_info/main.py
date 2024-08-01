# create user agent
from .user_agent import UserAgent as DefaultUserAgent
from .password import RandomStringManager as DefaultPasswordManager

class RealInfoManager:
    def __init__(self, user_agent_manager=None, password_manager=None, **kwargs):
        self.user_agent_manager = user_agent_manager or DefaultUserAgent()
        self.password_manager = password_manager or DefaultPasswordManager()
    
    def get_random_password(self, **kwargs):
        return self.password_manager.generate(**kwargs)
    
    def get_random_user_agent(self):
        return self.user_agent_manager.get_random_user_agent()

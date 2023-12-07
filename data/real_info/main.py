# create user agent
from .user_agent import UserAgent
from .password import RandomStringManager

class RealInfoManager:
    def __init__(self, **kwargs):
        ## managers
        self.user_agent_manager = UserAgent()
        self.password_manager = RandomStringManager()

        ## attrs
        self.user_agent = self.get_random_user_agent()
        self.password = self.get_random_password(**kwargs)
    
    def get_random_password(self, **kwargs):
        return self.password_manager(**kwargs)
    
    def get_random_user_agent(self):
        return self.user_agent_manager.get_random_user_agent()
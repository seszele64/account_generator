# create random user agent that will be used for browser and requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity, HardwareType

class UserAgentManager():

    def __init__(self, **kwargs):
        # set user agent parameters -> software_names, operating_systems, popularity, hardware_type
        self.user_agent_rotator = UserAgent()
        self.software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value, SoftwareName.OPERA.value] or kwargs.get('software_names')
        self.operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MACOS.value] or kwargs.get('operating_systems')
        self.popularity = [Popularity.POPULAR.value] or kwargs.get('popularity')
        self.hardware_type = [HardwareType.COMPUTER.value, HardwareType.MOBILE.value] or kwargs.get('hardware_type')
    
    def get_random_user_agent(self) -> str:
        user_agent_rotator = UserAgent(
            software_names=self.software_names,
            operating_systems=self.operating_systems,
            popularity=self.popularity,
            limit=100
        )
        return user_agent_rotator.get_random_user_agent()
    
    # get popular user agents
    
    # higher popularity -> more popular user agents
    def increase_popularity(
            self,
    ):
        # get index of current popularity -> increase it by 1 if possible, else return the same popularity and log that max popularity is reached
        current_popularity_index = self.popularity.index(Popularity.POPULAR.value)

        if current_popularity_index < len(self.popularity) - 1:
            self.popularity = self.popularity[current_popularity_index + 1]

            return self

        else:
            print('Max popularity reached')

    # lower popularity -> less popular user agents
    def lower_popularity(
            self
    ):
        # get index of current popularity -> decrease it by 1 if possible, else return the same popularity and log that min popularity is reached
        current_popularity_index = self.popularity.index(Popularity.POPULAR.value)

        if current_popularity_index > 0:
            self.popularity = self.popularity[current_popularity_index - 1]

        else:
            print('Min popularity reached')


# create random user agent
def generate_random_user_agent():
    return UserAgentManager().get_random_user_agent()
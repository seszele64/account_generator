# create random user agent that will be used for browser and requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity, HardwareType
def generate_random_user_agent(software_names=None, operating_systems=None, popularity=None, hardware_type=None):
    user_agent_rotator = UserAgent(
        software_names=software_names or [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value, SoftwareName.OPERA.value],
        operating_systems=operating_systems or [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MACOS.value],
        popularity=popularity or [Popularity.POPULAR.value],
        hardware_type=hardware_type or [HardwareType.COMPUTER.value, HardwareType.MOBILE.value]
    )
    return user_agent_rotator.get_random_user_agent()
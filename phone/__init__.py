from ..old_code.fivesim import FiveSimManager
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'Your token' with your actual API token
token = os.getenv("TOKEN")

# Create an instance of the FiveSim class
api = FiveSimManager(token)

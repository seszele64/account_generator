# Comments:
# Used packages: SQLAlchemy, Selenium, BeautifulSoup, dataclasses, datetime, re

# imports from random_info package -> __init__.py

# ----------------------------------- data ----------------------------------- #

from data import create_person, get_random_string, random_user_agent

# --------------------------------- SERVICES --------------------------------- #

# verification
from verification import (
    #mail
    check_link_inbox,
    # phone
    get_phone_number,
    get_verification_code
)

# asynchronic programming
import asyncio
import queue
import threading

# run in thread
def run_in_thread(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()

# create queue
q = queue.Queue()

# create person
person = create_person()
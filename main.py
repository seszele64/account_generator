# Comments:
# Used packages: SQLAlchemy, Selenium, BeautifulSoup, dataclasses, datetime, re

# imports from random_info package -> __init__.py

# ----------------------------------- INFO ----------------------------------- #

# random_info
from random_info import create_person

# real info

from database import table


# --------------------------------- SERVICES --------------------------------- #

# mail
from mail

# phone
from phone import api

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
# Comments:
# Used packages: SQLAlchemy, Selenium, BeautifulSoup, dataclasses, datetime, re

# imports from random_info package -> __init__.py

# ----------------------------------- INFO ----------------------------------- #

# random_info
from random_info import create_person
from data.random_info import (
    


# --------------------------------- SERVICES --------------------------------- #

# verification
from verification import (
    #mail
    create_mail_address,
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


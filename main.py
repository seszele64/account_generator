# Comments:
# Used packages: SQLAlchemy, Selenium, BeautifulSoup, dataclasses, datetime, re

# imports from random_info package -> __init__.py
from random_info import create_person
from database import table

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
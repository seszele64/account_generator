# use webshare.io to get proxies
# api gives me a list of proxies
# how to name a class -> Proxies

# imports
import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import json

# local imports
from proxy_db import ProxyDatabase, Database

# get proxies


class Proxy:

    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def __str__(self):
        return f"""
        ip: {self.ip}
        port: {self.port}
        username: {self.username}
        password: {self.password}
        """

    # to_dict

    def to_dict(self):
        return {
            'ip': self.ip,
            'port': self.port,
            'username': self.username,
            'password': self.password
        }

    # to_list
    def to_list(self):
        return [
            self.ip,
            self.port,
            self.username,
            self.password
        ]

    # to_json
    def to_json(self):
        return json.dumps(self.to_dict())


class ProxyList:

    def __init__(self, api_url):
        self.api_url = api_url

        # proxies
        self.proxy_list = []

        # run flow -> get_proxies, parse_proxies, set_proxies
        self.run_flow()

    # run flow -> get_proxies, parse_proxies, set_proxies

    def run_flow(self):
        # get proxies
        proxy_list_from_api = self.get_proxy_list_from_api()

        # parse proxies
        parsed_proxy_list = self.parse_proxy_list(proxy_list_from_api)

        # set proxies
        self.set_proxy_list(parsed_proxy_list)

    # get proxy list from api_url

    def get_proxy_list_from_api(self) -> list:
        # get proxies from self.api_url
        proxy_list = requests.get(self.api_url)
        # get response
        proxy_list = proxy_list.text
        # return
        return proxy_list

    # parse proxy list

    def parse_proxy_list(self, proxy_list) -> list:

        # parse proxy
        def parse_proxy(proxy) -> dict:
            # transform an element of proxies_list into a dictionary
            # split by ':'
            proxy = proxy.split(':')
            print(proxy)

            # create Proxy element
            parsed_proxy = Proxy(
                ip=proxy[0],
                port=proxy[1],
                username=proxy[2],
                password=proxy[3]
            )

            # return
            return parsed_proxy

        # transform proxies into a list of dictionaries
        proxy_list = proxy_list.split('\n')

        # create empty list
        parsed_proxy_list = []

        # iterate over proxies
        for proxy in proxy_list:

            # if proxy is empty
            if proxy == '':
                # continue
                continue

            # replace '\r' with ''
            proxy = proxy.replace('\r', '')

            # append to proxies_list
            parsed_proxy_list.append(
                parse_proxy(proxy)
            )

        # return
        return parsed_proxy_list

    # set proxies to list of Proxy elements

    def set_proxy_list(self, proxy_list):

        # del value of self.proxies
        del self.proxy_list

        # create list
        self.proxy_list = []

        # iterate over proxies
        for proxy in proxy_list:

            # append to self.proxies
            self.proxy_list.append(proxy)

    # str -> print proxy_list

    def __str__(self):
        return str(self.proxy_list)


class ProxySelector(ProxyList, ProxyDatabase):

    # init
    def __init__(self, api_url, db_name, table_name):
        # init ProxyList
        ProxyList.__init__(self, api_url)

        # init ProxyDatabase
        ProxyDatabase.__init__(self, db_name, table_name)
        self.add_proxies_to_database()

        # current proxy
        self.current_proxy = ProxyDatabase.get_random_proxy(self)

    # add proxies from proxy_list to database
    def add_proxies_to_database(self):
        # iterate over proxies
        for proxy in self.proxy_list:
            # add proxy to database
            ProxyDatabase.add_proxy(self, proxy)

    # get proxy by id
    def change_proxy(self, proxy_id):
        # query database using id
        proxy = proxy_db.get_proxy_by_id(proxy_id)

        # set self.current_proxy to proxy
        self.current_proxy = proxy

    # is there a next proxy
    def is_there_next_proxy(self):
        # get index of current proxy
        current_proxy_index = self.current_proxy[0]

        # use database not list

        # query database using id
        if proxy_db.get_proxy_by_id(current_proxy_index + 1) != None:
            return True

        return False

    # is there a previous proxy
    def is_there_previous_proxy(self):
        # get index of current proxy
        current_proxy_index = self.current_proxy[0]

        # use database not list

        # query database using id
        if proxy_db.get_proxy_by_id(current_proxy_index - 1) != None:
            return True

        return False

    # next proxy

    def next_proxy(self):

        # check if there is a next proxy
        if self.is_there_next_proxy():
            # get index of current proxy
            current_proxy_index = self.current_proxy[0]

            # change proxy to current_proxy_index + 1
            self.change_proxy(current_proxy_index + 1)
        else:
            # change proxy to 0
            self.change_proxy(0)

    # previous proxy

    def previous_proxy(self):
        # if there is a previous proxy
        if self.is_there_previous_proxy():
            # get index of current proxy
            current_proxy_index = self.current_proxy[0]

            # change proxy to current_proxy_index - 1
            self.change_proxy(current_proxy_index - 1)
        else:
            # change proxy to last proxy
            self.change_proxy(len(self.proxy_list) - 1)

    # str -> proxy_list ip:port, username, password
    def __str__(self):
        return str(self.current_proxy)


# init ProxyList
api_url = 'https://proxy.webshare.io/api/v2/proxy/list/download/nyufvzjqdtxygfnvdmdbbfjzkiesqvxlhsfqamoq/-/any/username/direct/-/'

# init ProxyDatabase
proxy_db = ProxySelector(api_url, 'proxy', 'proxy_list')
print(proxy_db)

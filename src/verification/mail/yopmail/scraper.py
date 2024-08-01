# bs4
import datetime
import requests
import re
import string
import random
from bs4 import BeautifulSoup

from typing import Optional
from random_user_agent.user_agent import UserAgent

class YopmailHTML:

    def __init__(self, html, username=None, mail_id=None):
        self.html = html
        self.mail_id = mail_id or ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(6)])
        self.username = username or ''

    def save(self, filename=None):
        filename = filename or f'{self.username}_{self.mail_id}.html'
        with open(filename, "w", encoding="utf8") as f:
            try:
                f.write(self.html)
                return True
            except Exception as err:
                print(f"[x] Couldn't save mail #{self.mail_id}:", err)
                return False

    def __repr__(self):
        return self.html

class YopmailScraper:
    def __init__(self, username: str, proxies: Optional[dict[str, str]] = None, user_agent: Optional[str] = None):
        self.username = username
        self.url = 'https://yopmail.com/'
        self.yp = None
        self.yj = None
        self.ycons = None
        self.ytime = None
        self.jar = requests.cookies.RequestsCookieJar()
        self.session = requests.Session()
        self.proxies = proxies
        self.user_agent = user_agent

    def request(self, url: str, params: Optional[dict[str, str]] = None, context: Optional[str] = None, headers: Optional[dict[str, str]] = None) -> requests.models.Response | None:
        """Make a request to yopmail.com

        Args:
            url (str): url to request
            params (dict[str, str], optional): parameters to include in the request. Defaults to None.
            context (str, optional): context of the request. Defaults to None.
            headers (dict[str, str], optional): headers to include in the request. Defaults to None.

        Returns:
            requests.models.Response | None: response object or None if request failed
        """
        try:
            if self.yp is None:
                context = 'yp'
                req = self.session.get(self.url, proxies=self.proxies)
                if not req:
                    return None
                self.extract_yp(req)
                params = {**params, 'yp': self.yp}

            if self.yj is None:
                context = 'yj'
                req = self.session.get(
                    'https://yopmail.com/ver/5.0/webmail.js', proxies=self.proxies)
                if not req:
                    return None
                self.extract_yj(req)
                params = {**params, 'yj': self.yj}

            if self.ycons is None:
                context = 'ycons'
                # Set consent cookies
                req = self.session.get(
                    'https://yopmail.com/consent?c=deny', proxies=self.proxies)
                if not req:
                    return None
            self.add_ytime()
            return self.session.get(url, params=params, cookies=self.jar, proxies=self.proxies, headers={'User-Agent': self.user_agent})

        # Error handling
        except requests.exceptions.ProxyError as err:
            print(f"[x] Couldn't process {context} request (ProxyError):", err)
            return None
        except requests.exceptions.ConnectionError as err:
            print(
                f"[x] Couldn't process {context} request (ConnectionError):", err)
            return None
        except requests.exceptions.Timeout as err:
            print(f"[x] Couldn't process {context} request (Timeout):", err)
            return None
        except Exception as err:
            print(f"[x] Couldn't process {context} request:", err)
            return None

    def add_ytime(self):
        now = datetime.datetime.now().time()
        self.ytime = f'{now.hour}:{now.minute}'
        self.jar.set('ytime', self.ytime, domain='yopmail.com', path='/')

    def extract_yp(self, req):
        # Looking for value of an hidden input element with 'yp' as name and id:
        #   <input type="hidden" name="yp" id="yp" value="XXX" />
        bs = BeautifulSoup(req.text, 'html.parser')
        el = bs.find('input', {'name': 'yp', 'id': 'yp'})
        self.yp = el['value']

    def extract_yj(self, req):
        # Looking for:
        #   value+'&yj=QBQVkAQVmZmZ4BQR0ZwNkAN&v='
        YJ_RE = re.compile(
            "value\+\'\&yj\=([0-9a-zA-Z]*)\&v\=\'", re.MULTILINE)
        match = YJ_RE.search(req.text)
        self.yj = match.groups()[0]

    def get_inbox(self, page=1) -> requests.models.Response | None:

        params = {
            'login': self.username,
            'p': str(page),  # page
            'd': '',        # mailid? to delete?
            'ctrl': '',     # mailid or ''
            'yp': self.yp,
            'yj': self.yj,
            'v': '8.4',
            'r_c': '',      # '' or recaptcha?
            # idaff / sometimes "none" / nextmailid='last' / mailid = id('m%d'%mail_nr)
            'id': '',
            'spam': True,   # False
            # 'scrl': '',
            # 'yf': '005',
        }
        return self.request(f'{self.url}inbox', params=params, context='inbox', headers={'User-Agent': self.user_agent})

    def get_mail_ids(self, page=1) -> list | None:
        # We're looking for mail ids:
        if req := self.get_inbox(page=page):
            bs = BeautifulSoup(req.text, 'html.parser')
            return [mail["id"] for mail in bs.find_all('div', {'class': 'm'})]

    def get_mail_body(self, mail_id: int, show_image=False) -> YopmailHTML:
        if show_image:
            mail_id = f'i{mail_id}'
        else:
            mail_id = f'm{mail_id}'
        params = {
            'b': self.username,
            # mail_id "{'i' to show images || 'm' to don't}e_ZGpjZGV1ZwRkZwD0ZQNjAmx0AmpkAj=="
            'id': mail_id
        }
        req = self.request(f'{self.url}mail', params=params, context='mail body', headers={'User-Agent': self.user_agent})
        mail_html = str(BeautifulSoup(
            req.text, 'html.parser').find('div', {'id': 'mail'}))
        return YopmailHTML(mail_html, self.username, mail_id)

    # read newest mail
    def read_newest_mail(self) -> YopmailHTML:
        mail_ids = self.get_mail_ids()
        if mail_ids:
            return self.get_mail_body(mail_ids[-1])
        return None

class YopmailManager:

    def __init__(self, proxies: Optional[dict[str, str]] = None):
        self.proxies = proxies
        self.user_agent_rotator = UserAgent()

    # set user agent
    def get_random_user_agent(self) -> str:
        return self.user_agent_rotator.get_random_user_agent()
    
    # create headers
    def get_headers(self, user_agent: Optional[str] = None) -> dict[str, str]:
        return {'User-Agent': user_agent or self.get_random_user_agent()}

    def get_newest_mail_for_username(self, username: str, proxies: Optional[dict[str, str]] = None) -> YopmailHTML:
        return YopmailScraper(username, proxies, self.get_random_user_agent()).read_newest_mail()
    
    def get_inbox_for_username(self, username: str, proxies: Optional[dict[str, str]] = None) -> requests.models.Response | None:
        return YopmailScraper(username, proxies, self.get_random_user_agent()).get_inbox()

    # get today's domain -> https://yopmail.com/domain?d=list
    def get_todays_domain(self, proxies=None, user_agent = None) -> list | None:

        # send request
        req = requests.get('https://yopmail.com/en/domain?d=list', proxies=proxies, headers=self.get_headers())
        bs = BeautifulSoup(req.text, 'html.parser')

        # get options under /html/body/select/optgroup[1]
        options = bs.find_all('optgroup')[0].find_all('option')
        return random.choice(options).text
    
    def get_mail_address_with_todays_domain(self, name: str, surname: str, proxies: Optional[dict[str, str]] = None) -> str:
        return f"{name}.{surname}{self.get_todays_domain(proxies=proxies)}"

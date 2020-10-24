import requests
from bs4 import BeautifulSoup


class Common(object):
    def __init__(self):
        super(Common, self).__init__()
        self.headers = ''
        self.session = requests.Session()
        self.previous_request_time = 0

    def http_get(self, url='', data='', auto_parse=False):
        # self.__anti_spam_protection()
        r = self.session.get(url=url, params=data, headers=self.session.headers)
        self.session.headers['Referer'] = r.url
        if auto_parse:
            r = self.response_parser(r)
        return r

    def http_post(self, url='', data='', params='', redirection=True, auto_parse=False):
        # self.__anti_spam_protection()
        r = self.session.post(url=url, params=params, data=data, headers=self.session.headers, allow_redirects=redirection)
        self.session.headers['Referer'] = r.url
        if auto_parse:
            r = self.response_parser(r)
        return r

    @staticmethod
    def response_parser(site):
        soup = BeautifulSoup(site.text, 'html.parser')
        return soup

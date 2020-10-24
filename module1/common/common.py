import time
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import configparser
import dateutil.parser
import datetime
import json


class Common(object):
    def __init__(self):
        super(Common, self).__init__()
        self.headers = ''
        self.session = requests.Session()
        self.previous_request_time = 0

    def http_get(self, url='', data='', auto_parse=False):
        self.__anti_spam_protection()
        r = self.session.get(url=url, params=data, headers=self.session.headers)
        self.session.headers['Referer'] = r.url
        if auto_parse:
            r = self.response_parser(r)
        return r

    def http_post(self, url='', data='', params='', redirection=True, auto_parse=False):
        self.__anti_spam_protection()
        r = self.session.post(url=url, params=params, data=data, headers=self.session.headers, allow_redirects=redirection)
        self.session.headers['Referer'] = r.url
        if auto_parse:
            r = self.response_parser(r)
        return r

    @staticmethod
    def message_out(msg):
        print(msg)

    @staticmethod
    def response_parser(site):
        soup = BeautifulSoup(site.text, 'html.parser')
        return soup

    @staticmethod
    def url_parse(url):
        query = urllib.parse.urlparse(url).query
        parsed_query = dict([x.split('=') for x in query.split('&')])
        return parsed_query

    @staticmethod
    def is_it_convertible_to_int(this):
        try:
            if type(this) is int:
                return this

            output = re.findall('[0-9]+', this)
            if type(output) is list:
                output = ''.join(output)
                if not output:
                    return None
                return output
            return None
        except:
            return None

    @staticmethod
    def find_targeting_attr(attr, data):
        output = []
        bool_ = list(map(lambda x: x.has_attr(attr), data))
        for element in bool_:
            if element:
                output.append(data[bool_.index(element)])

        if len(output) > 1:
            return output
        else:
            return output[0]

    @staticmethod
    def generate_date_format_from_custom_string(date, convert_to_str=True):
        if 'today' in date:
            date = datetime.datetime.now()
            date = date.strftime('%Y/%m/%d %H:%M')
            date = str(date)

        if 'yesterday' in date:
            date = datetime.datetime.now()
            date = date.today() - datetime.timedelta(days=1)
            date = date.strftime('%Y/%m/%d %H:%M')
            date = str(date)

        if 'mins' in date:
            digits = re.findall(r'[0-9]+', date)
            date = datetime.datetime.now()
            digits = int(''.join(digits))
            date = date.today() - datetime.timedelta(minutes=digits)
            date = str(date)

        if 'hrs' in date:
            digits = re.findall(r'[0-9]+', date)
            date = datetime.datetime.now()
            digits = int(''.join(digits))
            date = date.today() - datetime.timedelta(hours=digits)
            date = str(date)

        try:
            date = dateutil.parser.parse(date)
            if convert_to_str:
                date = str(date)
            return date
        except:
            return None

    @staticmethod
    def extract_value_from_list_of_dicts(key, list_of_dicts, filter_none=False):
        output = list(map(lambda x: x[key], list_of_dicts))
        if filter_none:
            output = list(filter(None, output))
        return output

    @staticmethod
    def remove_repeats_between_lists(input_list, second_input_list):
        new_collected_links = []
        for elem in input_list:
            if elem not in second_input_list:
                new_collected_links.append(elem)
        return new_collected_links

    def __anti_spam_protection(self):
        time_difference = time.time() - self.previous_request_time
        if time_difference < 5:
            time.sleep(5-time_difference)
            self.previous_request_time = time.time()
        else:
            self.previous_request_time = time.time()

    @staticmethod
    def count_medium_date_in_list_of_dates(list_of_dates):
        unix_time_total = 0
        for date in list_of_dates:
            unix_time = date.timestamp()
            unix_time_total = unix_time_total + unix_time
        medium_date = unix_time_total/len(list_of_dates)
        return datetime.datetime.utcfromtimestamp(medium_date)

    @staticmethod
    def time_now():
        return datetime.datetime.now()

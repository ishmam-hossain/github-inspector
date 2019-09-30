from os import path
from .utils import fetch_data, filter_data, colored_print


class UserInfo:
    __slots__ = ('BASE_URL', 'USER_URL', 'response_data')

    def __init__(self, user_name):
        self.BASE_URL = 'https://api.github.com/users/'
        self.USER_URL = path.join(self.BASE_URL, user_name)
        self.response_data = dict()

        self.print_in_terminal()

    @property
    def basic_info(self):
        basic_data = fetch_data(self.USER_URL)

        self.response_data.update(**filter_data(basic_data))
        return self.response_data

    def print_in_terminal(self):
        colored_print(self.basic_info)

from .utils import (fetch_data,
                    represent_repo_data,
                    filter_data,
                    filter_and_print_basic_info,
                    filter_and_print_repo_info
                    )
from threading import Thread
import concurrent.futures


class GitInspect:
    __slots__ = ('BASE_URL', 'response_data', 'user_name')

    def __init__(self, user_name):
        self.BASE_URL = 'https://api.github.com/users/'
        self.user_name = user_name
        self.response_data = dict()

        self.print_in_terminal()

    @property
    def repo_info(self):
        repo_data = fetch_data(base_url=self.BASE_URL,
                               user_name=self.user_name,
                               suffix='repos')

        return represent_repo_data(repo_data)

    @property
    def basic_info(self):
        basic_data = fetch_data(base_url=self.BASE_URL,
                                user_name=self.user_name)

        #   TODO: change response data
        self.response_data.update(**filter_data(basic_data))

        return self.response_data

    def print_in_terminal(self):
        filter_and_print_basic_info(self.basic_info)
        filter_and_print_repo_info(self.repo_info)

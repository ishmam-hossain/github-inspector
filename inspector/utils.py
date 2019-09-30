# from concurrent.futures import ThreadPoolExecutor
import requests
import shutil
from termcolor import colored


def get_all_urls(json_data):
    _urls = {
        data: json_data[data].split('{')[0]
        for data in json_data
        if isinstance(json_data[data], str) and json_data[data].startswith('https')
    }

    return _urls


def fetch_data(_url):
    return requests.get(_url).json()


def get_info_from_urls(json_data):
    url_list = get_all_urls(json_data)
    print(url_list)


def filter_data(json_data):
    wanted_fields = {
        'name',
        'login',
        'url',
        'type',
        'company',
        'location',
        'email',
        'hireable',
        'bio',
        'public_repos',
        'public_gists',
        'followers',
        'following',
        'created_at',
        'updated_at'

    }

    return {field: json_data[field] for field in wanted_fields}


def print_divider():
    # print(f"\n{colored('---' * 3, 'yellow')}\n")
    print("\n\n")


def colored_print(_data):
    print_fields = {
        'login',
        'url',
        'type',
        'company',
        'location',
        'email',
        'hireable',
        'bio',
        'public_repos',
        'public_gists',
        'followers',
        'following',
        'created_at',
        'updated_at'

    }
    max_size = len(max(print_fields, key=len))
    terminal_column = shutil.get_terminal_size().columns
    print_divider()
    print(colored(_data['name'].center(terminal_column), "white", 'on_red', attrs=['bold']))
    print_divider()

    for field in print_fields:
        print(colored(f"{field.replace('_', ' ').capitalize()}{' '* (max_size - len(field))}",
                      "white", "on_cyan", attrs=["bold"]), end="      ")
        print(colored(_data[field], "yellow"))

    print_divider()

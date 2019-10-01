import operator

import requests
import shutil
from termcolor import colored
from os import path
from collections import Counter


def get_all_urls(json_data):
    _urls = {
        data: json_data[data].split('{')[0]
        for data in json_data
        if isinstance(json_data[data], str) and json_data[data].startswith('https')
    }

    return _urls


def fetch_data(base_url, user_name, suffix=''):
    url_path = path.join(base_url, user_name, suffix).strip("/")
    return requests.get(url_path).json()


def filter_repo_data(repos):
    repo_details = list()
    for repo in repos:
        repo_detail = {
            "name": repo["name"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "description": repo["description"],
        }

        repo_details.append(repo_detail)

    return repo_details


def represent_repo_data(repo_data):
    repo_data = filter_repo_data(repo_data)
    total_stars = sum([_data["stars"] for _data in repo_data])
    used_languages = dict(Counter([_data["language"] for _data in repo_data]))
    most_used_language_count = max(used_languages.values())
    most_used_language = {max(used_languages.items(), key=operator.itemgetter(1))[0]: most_used_language_count}

    representational_data = {
        "total_stars": total_stars,
        "used_languages": used_languages,
        "most_used_language": most_used_language,
        "repo_data": repo_data
    }
    return representational_data


def get_info_from_urls(json_data):
    url_list = get_all_urls(json_data)

    for _url in url_list:
        print(fetch_data(_url, 'dummy'))


def filter_data(json_data):
    # deprecated
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


def print_divider(count=2):
    print("\n" * count)


def print_dict(_data, max_size):
    for field in _data:
        print(colored(f"{field.capitalize()}{' ' * (max_size - len(field))}",
                      "white", attrs=["bold", "dark", "underline"]), end="      ")
        print(colored(_data[field], "yellow"))

    print_divider(1)


def filter_and_print_basic_info(_data):
    print_fields = sorted({
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
    })

    max_size = len(max(print_fields, key=len))
    terminal_column = shutil.get_terminal_size().columns

    print_divider(1)
    print(colored(_data['name'].center(terminal_column), "white", 'on_red', attrs=['bold']))
    print_divider(0)

    printable_dict = {field: _data[field] for field in print_fields}

    print_dict(printable_dict, max_size)


def get_printable_string_from_dict(_data):
    return ", ".join([f"{key} ({_data[key]})" for key in _data])


def filter_and_print_repo_info(_data):
    max_size = len(max(_data.keys(), key=len))
    for key in sorted(_data):
        if key != "repo_data":
            print(
                colored(
                    f"{key.replace('_', ' ').capitalize()}{' ' * (max_size - len(key))}:   "
                    f"{_data[key] if not isinstance(_data[key], dict) else f'{get_printable_string_from_dict(_data[key])}'}"
                    f" {'✯' if key == 'total_stars' else ''} ",
                    "red", attrs=["bold", "dark", "underline"]
                ),
                end="     ")
            print()

    print_divider(1)

    max_size = len(max(_data.keys(), key=len))

    for repo in _data['repo_data']:
        print_dict(repo, max_size)



from requests import get as fetch_data
from sanic.views import HTTPMethodView
from sanic.response import json
from decouple import config
from os import path


BASE_URL = config('BASE_URL')
USER_URL = path.join(BASE_URL, 'users')


class UserOverView(HTTPMethodView):
    @staticmethod
    def get(self, user_name):

        user_data = fetch_data(path.join(USER_URL, user_name)).json()
        return json(user_data)

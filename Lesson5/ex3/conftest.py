import pytest
import requests

from .api.api_client import ApiClient




@pytest.fixture()
def basic_auth(request):
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")
    url = "https://httpbin.org/basic-auth/{}/{}".format(user, password)
    resp = requests.get(url).json()
    try:
        resp["authenticated"] is True
    except ConnectionError('Auth failed'):
        if resp['status_code'] == 401:
            print('Incorrect password or user')
        else:
            print("shit happens")


# 1. в conftest в Options получаем сервис который будем тестить

# в папке api создаем 3 разных файла (описание сервиса, который тестируем)

# импортируем эти объекты-сервисы в конфтест


# фикстура сервиса
@pytest.fixture()
def service():
    if pytest.addoption('url') == 'ya.ru':
        return ApiClient(host="")
# if url = 'ya.ru':
#   return ApiClinet_Yandex():
#



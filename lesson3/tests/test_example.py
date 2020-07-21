import requests


def test_example(url_data):
    url = f'https://www.w3schools.com/python/{url_data}.asp'
    response = requests.get(url=url)
    assert response.status_code == 200

import pytest
import requests


@pytest.mark.parametrize("test_input, expected_result", [(1, 2), (2, 4), (3, 6), (4, 8)])
def test_multiplication(test_input, expected_result):
    assert test_input * 2 == expected_result


@pytest.mark.parametrize("status_code, expected_response",
                         [(200, 200), (300, 300), (400, 400), (500, 500)])
def test_eval(status_code, expected_response):
    url = "https://httpbin.org/status/"
    response = requests.get(url + f"{status_code}")
    assert response.status_code == expected_response

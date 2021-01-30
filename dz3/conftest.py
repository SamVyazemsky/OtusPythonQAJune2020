import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com/todos",
        help="Request base url"
    )


@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def session():
    return requests.Session()

@pytest.fixture(params=[0, 201], scope="module")
def incorrect_todo_id(request):
    return request.param

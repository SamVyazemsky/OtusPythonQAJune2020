import pytest


def pytest_addoption(parser):
    parser.addoption('--path', action='store', default='..//homework7//apache_log.txt')


@pytest.fixture
def path_to_file(request):
    return request.config.getoption('--path')


import pytest
from logging import log


def pytest_generate_tests(metafunc):
    if "fixture1" in metafunc.fixturenames:
        metafunc.parametrize("fixture1", [
            1, 2, 3, 4, 5, 6, 7, 8, 9

        ])
    if "fixture2" in metafunc.fixturenames:
        metafunc.parametrize("fixture2", [
            2, 3, 4, 5, 6, 7, 8, 9
        ])

    # Открываем выбранный файл
    with open("test", 'r') as f:
        test_case = f.__next__()

    #
    return metafunc.parametrize("urls", test_case)


def test_status_code(fixture1, fixture2, urls):

    assert fixture1 + fixture2 > len(urls)


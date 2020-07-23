import pytest
from logging import log


@pytest.fixture()
def open_file():
    f = open("test")
    try:
        yield f

    finally:
        f.close()


@pytest.fixture()
def read_file(open_file):
    res = []
    for each in open_file:
        res.append(each.replace('\n', ''))
    return res


@pytest.mark.parametrize('tests_from_file', read_file)
def test_open_file(tests_from_file):
    assert tests_from_file == "test1"

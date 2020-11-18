import pytest


@pytest.fixture(params=[20, 12, 1, 4, 3])
def fixture(request):
    return request.param

@pytest.mark.parametrize('value', [4, 8, 15, 16, 23])
def test_List(value):
    list = [20, 12, 1, 4, value]
    list.reverse()
    assert list == [value, 4, 1, 12, 20]

def test_set(fixture):
    set = {35, 57, 86, 36, fixture}
    set2 = {20, 12, 1, 4, 3}
    set3 = set.intersection(set, set2)
    assert set3 == {fixture}

@pytest.mark.parametrize('city', ["msk", "spb", "ekb", "nsk", "irk"])
def test_dictionary(city):
    dict = {}
    dict[city] = city
    assert dict.pop(city) == city

@pytest.mark.parametrize('color', ["red", "green", "blue", "white", "black"])
def test_string(color):
    s = color
    assert s.isalpha() == True
    
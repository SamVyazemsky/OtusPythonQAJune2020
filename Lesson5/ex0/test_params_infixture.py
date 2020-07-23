import pytest


# @pytest.fixture(params=["one", "uno"])
# def fixture1(request):
#     return request.param
#
#
# @pytest.fixture(params=["two", "duo", "tres"])
# def fixture2(request):
#     return request.param
#
#
# def test_params_infixture(fixture1, fixture2):
#     assert type(fixture1) == type(fixture2)


@pytest.fixture(params=[1, 2, 3])
def fixture3(request):
    return request.param


@pytest.fixture(params=[2, 3, 4, 5])
def fixture4(request):
    return request.param


@pytest.mark.parametrize("expected", [1, 2, 3, 4, 5])
def test_params_infixture(fixture3, fixture4, expected):
    assert fixture3 + fixture4 > expected
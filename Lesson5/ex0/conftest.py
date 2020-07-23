import pytest


@pytest.fixture(params=[1, 2, 3])
def fixture3(request):
    return request.param


@pytest.fixture(params=[20, 30, 40, 50])
def fixture4(request, fixture3):
    return request.param, fixture3


@pytest.fixture(params=[2, 3, 4, 5])
def fixture5(request, fixture4):
    return request.param, fixture4


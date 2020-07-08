import pytest


@pytest.fixture(params=[11, 12, 13, 14])
def fixture_one(request):
    return request.param


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_two(request):
    return request.param
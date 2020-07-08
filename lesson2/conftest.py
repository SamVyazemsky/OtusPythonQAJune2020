import pytest

# @pytest.fixture()
# def first_fixture():
#     print("\nPrint from 'first_fixture' in conftest.py root")


# https://www.youtube.com/watch?v=7KgihdKTWY4&t=1s



@pytest.fixture
def first_fixture():
    print("\nPrint from 'first_fixture' in other conftest.py")


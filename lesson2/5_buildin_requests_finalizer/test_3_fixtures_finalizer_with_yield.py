import pytest


@pytest.fixture(scope="function")
def setup_function_fixture():
    print("\nHello from setup function fixture!\n")
    yield
    print("\nBye bye from setup function fixture!\n")


@pytest.fixture(scope="module")
def setup_module_fixture():
    print("\nHello from setup module fixture!\n")
    yield
    print("\nBye bye from setup module fixture!\n")


def test_one(setup_function_fixture):
    print(">>> Test Function Yield")
    pass


def test_two(setup_module_fixture):
    print(">>> Test Module Yield")
    pass

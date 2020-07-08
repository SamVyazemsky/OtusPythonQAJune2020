import pytest
import random
import math


@pytest.fixture
def fixture_return_rnd_number():
    return random.randint(1, 100), random.randint(10,50), random.randint(20,21)


class TestClass:

    def __init__(self, mod1, mod2):
        self.mod1 = mod1
        self.mod2 = mod2

    def hello(self, name):
        return f"Hello, {name}"


@pytest.fixture
def fixture_return_class():
    return TestClass(mod1=random, mod2=math)

# @pytest.fixture
# def driver():
#     pass
#
# @pytest.fixture
# def application():
#     return MainPage(driver), LoginPage(driver), BasketPage(driver)
#

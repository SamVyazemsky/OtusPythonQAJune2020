import pytest


# @pytest.mark.parametrize("test_input", [(1, 1), (2, 2), (3, 3), (4, 4)])
# def test_one_2(test_input):
#     assert 0 == test_input[0] - test_input[1]
#     #print(test_input)
#
# #
# @pytest.mark.parametrize("test_input", [1, 2, 3])
# class TestClassParametrized:
#
#     # Все функци должны использовать аргумент
#     def test_one(self, test_input):
#         pass
#
#     def test_two(self, test_input):
#         pass


# Parametrize with fixture

# def test_one_1(fixture_one):
#     print(fixture_one)

# Combine parametrization
#
@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(fixture_two, fixture_one, test_input):
    print(fixture_one, fixture_two, test_input)

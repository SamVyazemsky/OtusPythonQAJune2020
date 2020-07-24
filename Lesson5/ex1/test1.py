import pytest


@pytest.mark.newaccount
@pytest.mark.test
def test_multiplication(test_input, expected_result):
    assert test_input * 2 == expected_result


@pytest.mark.xmlfile
@pytest.mark.parametrize("test_input_new, expected_result", [(1, 2), (2, 4), (3, 6), (16, 32)])
def test_without_file(test_input_new, expected_result):
    assert test_input_new * 2 == expected_result

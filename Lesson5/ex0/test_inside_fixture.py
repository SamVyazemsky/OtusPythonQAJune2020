import pytest


# ([1, 2, 3], [2, 3, 4, 5])
def test_params_infixture(fixture5):
    assert fixture5[1] + fixture5[0] > fixture5[2]
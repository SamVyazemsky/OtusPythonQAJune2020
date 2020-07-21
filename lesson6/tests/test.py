import pytest

from base.nums import Numbers


class Tests:

    @pytest.mark.parametrize("vars_", argvalues=[(5, 23), (45, 117)])
    def test_add_nums(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Numbers(a, b)
        sum = a + b
        assert num.sum() == sum

    @pytest.mark.parametrize("vars_", argvalues=[(5, 23), (375, 164)])
    def test_multi(self, vars_):
        a = vars_[0]
        b = vars_[1]
        num = Numbers(a, b)
        multi = a * b
        assert num.multi() == multi

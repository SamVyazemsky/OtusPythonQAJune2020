def test_the_number(fixture_return_rnd_number):
    first = fixture_return_rnd_number[0]
    second = fixture_return_rnd_number[1]
    third = fixture_return_rnd_number[2]
    assert first == 20 or second == 20 or third == 20


def test_the_class(fixture_return_class):

    assert fixture_return_class.mod2.pow(2, 3) == 8
    assert fixture_return_class.mod1.choice(['a', 'b', 'c']) == 'a'


def test_the_class2(fixture_return_class):
    assert fixture_return_class.hello('Vasya') == 'Hello, Vasya'

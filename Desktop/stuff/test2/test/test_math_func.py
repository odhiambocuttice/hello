import math_func


def test_Add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


def test_Add_strings():
    result = math_func.add('hello', ' world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'hello' in result


def test_product_strings():
    assert math_func.product('hello ', 3) == 'hello hello hello '
    result = math_func.product('hello ')
    assert result == 'hello hello '
    assert type(result) is str
    assert 'hello' in result

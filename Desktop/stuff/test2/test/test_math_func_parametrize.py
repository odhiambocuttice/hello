import math_func
import pytest


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (8, 2, 10),
                             ('hello', ' world', 'hello world'),
                             (20.3, 25.5, 45.8)

                         ]
                         )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result

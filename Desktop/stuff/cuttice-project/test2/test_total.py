import matlib


def test_total():
    total = matlib.calc_total(9, 0)
    assert total == 9


def test_mutiply():
    total = matlib.mutiply_total(9, 0)
    assert total == 0

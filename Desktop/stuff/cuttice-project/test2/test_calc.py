import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        # result = calc.subtract(10, 5)
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        # result = calc.subtract(10, 5)
        self.assertEqual(calc.multiply(6, 3), 18)

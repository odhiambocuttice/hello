import unittest
import mult


class TestMult(unittest.TestCase):

    def test_multiply(self):

        result = mult.multip(10, 8)
        self.assertEqual(result, 80)

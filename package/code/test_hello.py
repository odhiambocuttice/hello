import hello
import unittest


class Test_hello(unittest.TestCase):
    def test_hello(self):
        self.hello_mes = "hello curtis"


def test_print(self):
    ouput = hello.hello()
    assert(ouput == self.hello_mes)

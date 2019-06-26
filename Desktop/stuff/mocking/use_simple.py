from unittest import mock

import simple


# def use_simple_function():
#     result = simple.simple_function()
#     print(result)


# use_simple_function()
@mock.patch('simple.simple_function')
def mock_simple_function(mock_simple_func):  # magic object
    print(mock_simple_func)
    print(simple.simple_function)
    result = simple.simple_function()
    print(result)


mock_simple_function()

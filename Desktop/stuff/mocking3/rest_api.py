import unittest
from mock import Mock, patch
import requests
import api


class Test_Api(unittest.TestCase):

    def test_api(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert api() == 200

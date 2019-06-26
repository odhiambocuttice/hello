# configure mock

from mock import Mock
mock=Mock()
attrs = {'method.return_value': 89, 'error.side_effect': KeyError}
mock.configure_mock(**attrs)

print(mock.method())

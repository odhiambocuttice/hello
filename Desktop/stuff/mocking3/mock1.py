from mock import Mock
mock = Mock(return_value=1)
team = mock(1, 5, people='kenyans')
print(team)

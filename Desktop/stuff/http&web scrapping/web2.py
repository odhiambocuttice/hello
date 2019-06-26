import requests

payload = {'user_name': 'admin', 'password': 'password'}
r = requests.get('http://httpbin.org/get',
                 params=payload, allow_redirects=False, timeout=1)

print(r.url)
print(r.text)

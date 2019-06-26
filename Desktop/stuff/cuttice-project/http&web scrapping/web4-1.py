import requests

r = requests.get('http://httpbin.org/get')
print(r.headers['Access-Control-Allow-Credentials'])
print(r.headers['Access-Control-Allow-Origin'])
print(r.headers['CONNECTION'])
print(r.headers['content-length'])
print(r.headers['Content-Type'])
print(r.headers['Date'])
print(r.headers['server'])
print(r.headers['via'])

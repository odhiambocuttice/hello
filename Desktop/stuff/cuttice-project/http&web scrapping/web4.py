import requests

r = requests.get('http://httpbin.org/get')
print(r.encoding)

response = r.json()
print(r.json())
print(response['args'])
print(response['headers'])
print(response['headers']['Accept'])
print(response['headers']['Accept-Encoding'])

print(response['headers']['Host'])
print(response['headers']['User-Agent'])
print(response['origin'])
print(response['url'])

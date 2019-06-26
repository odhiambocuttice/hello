import requests

url = 'http://httpbin.org/post'
file_list = [
    ('image', ('flower1.jpg', open('flower1.jpg', 'rb'), 'image/png')),
    ('image', ('flower2.jpg', open('flower2.jpg', 'rb'), 'image/png'))
]

r = requests.post(url, files=file_list)
print(r.text)

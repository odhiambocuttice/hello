import requests

i = requests.get('https://imgs.xkcd.com/comics/python.png')


with open('flower2.png', 'wb') as f:
    f.write(i.content)

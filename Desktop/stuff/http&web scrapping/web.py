import requests


# t = requests.get('https://xkcd.com/353/')

r = requests.get('http://httpbin.org/get')

outfile = open('/home/cuttice/Desktop/http&web scrapping/i6.txt', 'w')
outfile.write(r.text)

print(r.headers)
print(r.is_redirect)
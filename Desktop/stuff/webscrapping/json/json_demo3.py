import json
import requests


r = requests.get("https://jsonplaceholder.typicode.com/todos")
t = json.loads(r.text)
print(type(t[67]))
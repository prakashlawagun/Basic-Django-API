import requests

URL ="http://127.0.0.1:8000/stdinfo/"

r= requests.get(URL)
data = r.json()
print(data)
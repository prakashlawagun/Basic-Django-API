import requests
import json

URL = "http://127.0.0.1:8000/stdapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

#
# get_data(1)


def post_data():
    data = {
        'name': 'Rohit',
        'roll': 201,
        'city': 'biratnagar',
    }

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id': 3,
        'name': 'Arav',
        'city': 'ktm',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {'id': 4}
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# delete_data()  in next we will not use third party app insted of it we will use browser api

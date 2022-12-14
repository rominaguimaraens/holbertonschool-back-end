#!/usr/bin/python3
"""
Python interpreter
"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    get_name = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(
        url,
        params={'userId': int(user_id)}).json()
    user_response = requests.get(get_name).json()

    container = {"{}".format(sys.argv[1]): []}
    key = "{}".format(sys.argv[1])
    for task in response:
        to_dump = {}
        to_dump['task'] = task.get('title')
        to_dump['completed'] = task.get('completed')
        to_dump['username'] = user_response.get('username')
        container[key].append(to_dump)
        with open("{}.json".format(sys.argv[1]), 'w+') as f:
            json.dump(container, f)

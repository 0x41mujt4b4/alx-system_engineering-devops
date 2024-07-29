#!/usr/bin/python3
"""
python module to send api request to todo list api data
"""
import csv
import json
import requests
from sys import argv


def main():
    """the main function of the module"""
    to_json = []
    id = ''
    try:
        id = int(argv[1])
    except Exception:
        id = ''

    todo_url = f"https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"

    todo_res = requests.get(url=todo_url)
    user_res = requests.get(url=user_url)

    todo_data = todo_res.json()
    user_data = user_res.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for task in todo_data:
        if task.get('userId') == id:
            TOTAL_NUMBER_OF_TASKS += 1
            row = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_data.get('username')
                   }
            to_json.append(row)
    with open(f'{id}.json', 'w') as file:
        file.writelines(json.dumps({f"{id}": to_json}))


if __name__ == '__main__':
    main()

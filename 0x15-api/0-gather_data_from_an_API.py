#!/usr/bin/python3
"""
python module to send api request to todo list api data
"""
import requests
from sys import argv


def main():
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
        if task['userId'] == id:
            TOTAL_NUMBER_OF_TASKS += 1
        if task['userId'] == id and task['completed']:
            NUMBER_OF_DONE_TASKS += 1
    print(f"Employee {user_data['name']} is done with tasks", end='')
    print(f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in todo_data:
        if task['userId'] == id and task['completed']:
            print(f"\t {task['title']}")


if __name__ == '__main__':
    main()

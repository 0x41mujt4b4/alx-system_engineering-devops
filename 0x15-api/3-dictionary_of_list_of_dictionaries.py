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

    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users"

    todos_res = requests.get(url=todos_url)
    users_res = requests.get(url=users_url)

    todos_data = todos_res.json()
    users_data = users_res.json()

    all_users = {}
    for user in users_data:
        userId = user.get('id')
        user_todos = []
        for task in todos_data:
            if task.get('userId') == userId:
                row = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                       }
                user_todos.append(row)
        all_users[str(userId)] = user_todos
    with open(f'todo_all_employees.json', 'w') as file:
        file.writelines(json.dumps(all_users))


if __name__ == '__main__':
    main()

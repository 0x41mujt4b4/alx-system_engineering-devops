#!/usr/bin/python3
"""
python module to send api request to todo list api data
"""
import requests
from sys import argv
import csv


def main():
    """the main function of the module"""
    to_csv = []
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
            row = [str(id), user_data.get('username'),
                   str(task.get('completed')), task.get('title')]
            to_csv.append(row)
    with open(f'{id}.csv', 'w') as file:
        write = csv.writer(file)
        write.writerows(to_csv)


if __name__ == '__main__':
    main()

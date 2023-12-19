#!/usr/bin/python3
"""Gather data from an API"""


import requests
import sys


def print_todo_progress(employee_id):
    """Prints the progress of a given employee"""
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = user_response.json()['name']

    todo_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    tasks = todo_response.json()

    total_tasks = len(tasks)
    done_tasks = sum(1 for task in tasks if task['completed'])

    print(
        f'Employee {employee_name} is done with tasks(
            {done_tasks}/{total_tasks}): ')
    for task in tasks:
        if task['completed']:
            print('\t ' + task['title'])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    print_todo_progress(employee_id)
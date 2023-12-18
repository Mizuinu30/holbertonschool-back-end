#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    user_id = sys.argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(user_id)).json()

    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'], len(done_tasks), total_tasks))

    for task in done_tasks:
        print('\t {}'.format(task['title']))
else:
    print("Usage: {} <employee_id>".format(sys.argv[0]))

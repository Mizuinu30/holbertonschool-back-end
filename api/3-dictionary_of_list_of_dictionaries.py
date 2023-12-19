#!/usr/bin/python3
"""Script to export data in the JSON format"""

import json
import requests
from sys import argv


def information_employee(id_employee):
    """Returns information about employees"""
    employee_name = ""
    task_data = []

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_one = requests.get(url_users)
    response_two = requests.get(url_todos)

    if response_one.status_code == 200:
        response_json_usr = response_one.json()
        response_json_tod = response_two.json()

        for user in response_json_usr:
            if user['id'] == id_employee:
                employee_name = user['username']

                for tod in response_json_tod:
                    if tod['userId'] == id_employee:
                        task_data.append(tod)

        # Call the function to export data to JSON
        export_to_json(id_employee, employee_name, task_data)

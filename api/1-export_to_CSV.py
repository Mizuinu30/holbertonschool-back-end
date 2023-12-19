#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to fetch data
about a specific employee
and exports a summary of the tasks to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    data = user_response.json()
    employee_name = data['name']

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_data = todos_response.json()

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            taskwriter.writerow(
                [employee_id, employee_name, task['completed'], task['title']])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    export_to_csv(employee_id)

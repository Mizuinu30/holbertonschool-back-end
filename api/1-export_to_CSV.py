#!/usr/bin/python3
"""Script to return info about todo list progress in csv format"""

import csv
import requests
from requests import get
from sys import argv


def information_employee(id_employee):
    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{id_employee}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data['username']

    # Get TODO data
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={id_employee}"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare data for CSV
    data = []
    for task in todo_data:
        data.append([id_employee, username, task['completed'], task['title']])

    # Write data to CSV
    with open(f"{id_employee}.csv", "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(data)


if __name__ == "__main__":
    information_employee(argv[1])

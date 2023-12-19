#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list for the employee
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    # Display progress information
    print(
        f"Employee {user_data['name']} is done with tasks
        ({done_tasks}/{total_tasks}): ")
    print(f"\t{user_data['name']}: {done_tasks}/{total_tasks}")

    # Display completed task titles
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

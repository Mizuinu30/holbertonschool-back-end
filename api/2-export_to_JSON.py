#!/usr/bin/python3
"""Script to return info about todo list progress and export data in JSON format"""
import requests
import json
from sys import argv


def get_user_data(user_id):
    """Get user data from the API"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(user_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting user data. Status code: {response.status_code}")
        return None


def get_todo_data(user_id):
    """Get todo data from the API"""
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url_todos)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting todo data. Status code: {response.status_code}")
        return None


def export_to_json(user_id, tasks):
    """Export tasks to JSON file"""
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(tasks, json_file, indent=2)
    print(f"Data exported to {filename}")


def information_employee():
    """Returns information about employees and exports tasks to JSON"""
    if len(argv) < 2:
        print("Usage: python script.py <employee_id>")
        return

    id_employee = int(argv[1])
    employee_data = get_user_data(id_employee)

    if employee_data:
        employee_name = employee_data['name']
        number_of_done_task = 0
        total_number_of_task = 0
        task_data = []

        todo_data = get_todo_data(id_employee)

        if todo_data:
            for todo in todo_data:
                if todo['userId'] == id_employee:
                    total_number_of_task += 1
                    task_info = {
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": employee_name
                    }
                    task_data.append(task_info)
                    if todo['completed']:
                        number_of_done_task += 1

            print(
                f'Employee {employee_name} is done with tasks ({number_of_done_task}/{total_number_of_task}):')
            for task in task_data:
                print(
                    f'\tTask: {task["task"]}, Completed: {task["completed"]}, Username: {task["username"]}')

            export_to_json(id_employee, task_data)


if __name__ == "__main__":
    information_employee()

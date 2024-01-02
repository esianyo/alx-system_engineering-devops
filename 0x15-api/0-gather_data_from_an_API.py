#!/usr/bin/python3
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = response.json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}').json()

    done_tasks = [task for task in todos if task['completed'] is True]
    total_tasks = len(todos)

    print(f"Employee {employee['name']} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print("\t " + task['title'])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 script.py <employee_id>')
    else:
        get_employee_todo_list_progress(sys.argv[1])

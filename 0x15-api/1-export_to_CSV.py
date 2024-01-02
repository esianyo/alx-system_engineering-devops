#!/usr/bin/env python3
"""
Python script to fetch and export TODO list progress for a given employee ID.

Usage:
    ./export_to_CSV.py <employee_id>
"""

import requests
import csv
from sys import argv


def fetch_employee_data(employee_id):
    """
    Fetch user and TODOs data for a given employee ID.

    Args:
        employee_id (int): Employee ID to fetch data for.

    Returns:
        Tuple: A tuple containing user data and a list of completed tasks.
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    user_response = requests.get(user_url)

    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("User not found")
        exit(1)

    if todos_response.status_code != 200:
        print("Todos not found")
        exit(1)

    user = user_response.json()
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task['completed']]

    return user, completed_tasks


def export_to_csv(user, completed_tasks, csv_filename):
    """
    Export user's completed tasks to a CSV file.

    Args:
        user (dict): User data.
        completed_tasks (list): List of completed tasks.
        csv_filename (str): CSV file name to export data to.
    """
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in completed_tasks:
            writer.writerow({
                'USER_ID': user['id'],
                'USERNAME': user['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })

    print("Data exported to {}".format(csv_filename))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    user, completed_tasks = fetch_employee_data(employee_id)

    csv_filename = '{}.csv'.format(user['id'])

    export_to_csv(user, completed_tasks, csv_filename)

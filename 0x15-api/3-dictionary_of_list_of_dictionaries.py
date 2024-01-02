#!/usr/bin/python3
'''
Script that exports an employee TODO tasks
'''
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_data = {}
        for user in users_data:
            todos_url = f"{base_url}/todos?userId={user['id']}"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            all_data[user['id']] = [{"username": user['username'], "task": task['title'], "completed": task['completed']} for task in todos_data]

        json_file = "todo_all_employees.json"
        with open(json_file, 'w') as file:
            json.dump(all_data, file)

        print(f"Data exported to {json_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

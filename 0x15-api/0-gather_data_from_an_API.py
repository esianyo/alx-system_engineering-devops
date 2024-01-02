import requests
from sys import argv


def fetch_employee_data(emp_id):
    # Fetch user data
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                 .format(emp_id))
    # Fetch TODOs for the given employee
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                                  .format(emp_id))

    # Check if user and TODOs are found
    if response.status_code != 200:
        print("User not found")
        exit(1)

    if response.status_code != 200:
        print("Todos not found")
        exit(1)

    # Extract user and TODOs data
    user = response.json()
    todos = todos.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task['completed']]

    return user, completed_tasks, todos


def display_employee_progress(user, completed_tasks, total_tasks):
    # Display employee progress information
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(completed_tasks), total_tasks))

    # Display titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    # Get employee ID from command line argument
    employee_id = int(argv[1])

    # Fetch employee data
    user, completed_tasks, todos = fetch_employee_data(employee_id)

    # Display employee progress
    display_employee_progress(user, completed_tasks, len(todos))

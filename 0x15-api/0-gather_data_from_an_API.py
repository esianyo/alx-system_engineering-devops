#!/usr/bin/python3

'''
Script that displays an employee completed TODO tasks
'''


if __name__ == "__main__":

    """import modules"""
    import requests
    import sys

    """send request"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]

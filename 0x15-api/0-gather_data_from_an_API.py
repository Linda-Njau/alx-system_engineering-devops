#!/usr/bin/python3
"""
Python script that uses the REST API and returns information about a given employee ID
and returns TODO list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    complete_tasks = []
    for task in todo:
        if task.get('completed') is True:
            complete_tasks.append(task.get('title'))
    print("Employee {} is done with task({}/{}):".
          format(user.get('name'), len(complete_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in complete_tasks))

#!/usr/bin/python3
"""
This script uses REST API to get todo list based
on employee id and returns a json file of the data
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(employee_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                                format(employee_id), verify=False).json()
    username = employee.get('username')
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todo]}, jsonfile)

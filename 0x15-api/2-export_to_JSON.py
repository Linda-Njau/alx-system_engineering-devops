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
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    json_obj = {}
    json_obj[employee_id] = tasks
    with open("json".format(employee_id), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)

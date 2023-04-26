#!/usr/bin/python3
"""
This script uses REST APU and return todo list info on an employee based
on their ID and returns the data using csv formats
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(employee_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(employee_id), verify=False).json()
    with open("{}.csv".format(employee_id), 'w', newline='') as csvfile:
        task_csv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            task_csv.writerow([int(employee_id), employee.get('username'),
                              task.get('completed'),
                              task.get('title')])

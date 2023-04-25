#!/usr/bin/python3
"""
This script uses a REST API to retrieve employee information and their todo list progress using their employee ID
"""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])
    total = 0
    completed = 0
    employee_url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    
    employee_name = (requests.get(employee_url)).json().get("name")
    tasks = requests.get(tasks_url)
    for task in tasks.json():
        if (task.get("userId") == employee_id):
            total +=1
            if (task.get("completed")):
                completed += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed, total))
    for task in tasks.json():
        if (task.get("userId") == employee_id):
            if (task.get("completed")):
                print("\t " + task.get("title"))

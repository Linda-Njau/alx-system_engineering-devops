#!/usr/bin/python3
"""
This script uses a REST API to retrieve employee information and their todo list progress using their employee ID
"""
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    employee_id = sys.argv[1]
    
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id), verify=False).json()
    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id), verify=False).json()
    completed_tasks = [todo for todo in todo_list if todo['completed']]
    num_completed = len(completed_tasks)
    num_total = len(todo_list)
    print("Employee {} is done with tasks ({}/{}):".format(user['name'], num_completed, num_total))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

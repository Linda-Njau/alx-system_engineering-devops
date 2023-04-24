#!/usr/bin/python3
"""
This script uses a REST API to retrieve employee information and their todo list progress using their employee ID
"""
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id), verify=False)
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id), verify=False)
    user = user_response.json()
    todo_list = todo_response.json()
    completed_tasks = [todo for todo in todo_list if todo['completed']]
    num_completed = len(completed_tasks)
    num_total = len(todo_list)
    print("Employee {} is done with tasks ({}/{}):".format(user['name'], num_completed, num_total))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

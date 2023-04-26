#!/usr/bin/python3
"""
This script exports to-do list from a REST API with information
on all employees based on id to JSON format
"""
import json
import requests

employees = requests.get("https://jsonplaceholder.typicode.com/users").json()
with open("todo_all_employees.json", "w") as jsonfile:
    json.dump({
        employee.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee.get("username"),
        } for task in requests.get("https://jsonplaceholder.typicode.com/todos",
                                   params={"userId":
                                           employee.get("id")}).json()]
        for employee in employees}, jsonfile)

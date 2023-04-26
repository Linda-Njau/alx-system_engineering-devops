#!/usr/bin/python3
"""
This script exports to-do list from a REST API with information
on all employees based on id to JSON format
"""
import json
import requests

url = "https://jsonplaceholder.typicode.com/"
employees = requests.get(url + "users").json()
with open("todo_all_employees.json", "w") as jsonfile:
    json.dump({
        employee.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee.get("username")s
        } for task in requests.get(url + "todos",
                                   params={"userId":
                                           employee.get("id")}).json()]
        for employee in employees}, jsonfile)

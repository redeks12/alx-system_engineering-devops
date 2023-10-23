#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given 
employee ID, returns information about his/her TODO list progress."""
import requests
from sys import argv
import json

tasks = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"userId": "{}".format(argv[1])},
)
todos = tasks.json()
response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
user_ = response.json()

with open("USER_ID.json", "w", encoding="utf-8") as f:
    fd = [
        {
            "task": {
                "task": to.get("title"),
                "completed": to.get("completed"),
                "username": user_.get("name"),
            }
        }
        for to in todos
    ]
    json.dump({user_.get("id"): fd}, f)
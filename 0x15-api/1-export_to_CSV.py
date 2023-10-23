#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given 
employee ID, returns information about his/her TODO list progress."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": "{}".format(argv[1])},
    )
    todos = tasks.json()
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    )
    user_ = response.json()

    with open("{}.csv".format(user_.get("id")), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, quotechar='"')
        for to in todos:
            writer.writerow(
                [
                    "{}".format(to.get("userId")),
                    "{}".format(user_.get("name")),
                    "{}".format(to.get("completed")),
                    "{}".format(to.get("title")),
                ]
            )

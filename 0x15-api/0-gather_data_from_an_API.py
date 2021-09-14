#!/usr/bin/python3
"""  script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    tasks = 0
    completed = 0
    completed_tasks = []
    r = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                     .format(argv[1])).json()

    r2 = requests.get('https://jsonplaceholder.typicode.com/todos/userId={:}'
                      .format(argv[1])).json()

    for task in r2:
        tasks += 1
        if task.get('completed') is True:
            completed += 1
            completed_tasks.append(task.get('title'))
    print("Employee {:} is done with tasks({:}/{:}):".format(
        r.get('name'), completed, tasks))
    for item in completed_tasks:
        print("\t {:}".format(item))

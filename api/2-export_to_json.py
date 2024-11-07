#!/usr/bin/python3
'''
a python script that uses utilizes an api to fetch an employee by
their id and finds all records of their tasks and writes them to a json file

- output filename: `USER_ID.json`
- format (without newlines):
    { "USER_ID": [
        {
        "task": "TASK_TITLE",
        "completed": "TASK_COMPLETED_STATUS",
        "username": "USERNAME"
        }, {
        "task": "TASK_TITLE",
        "completed": "TASK_COMPLETED_STATUS",
        "username": "USERNAME"
        }, ...
    ]}
'''

import json
from json.decoder import JSONDecoder
import requests
from sys import argv


def process_request():
    '''
    takes an integer representing a employee id from argv and writes the found
    employee's todo list data in cvs data format to a file
    ----
    "id","username","completion_status","task_title"
    ----
    '''
    if len(argv) < 2:
        print("no employee id provided")
        return

    given_id = argv[1]
    try:
        given_id = int(given_id)
    except ValueError:
        print("invalid employee id provided")
        return

    employee_get = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{given_id}")
    tasks_get = requests.get(
            "https://jsonplaceholder.typicode.com/todos")

    if employee_get.status_code != 200 or tasks_get.status_code != 200:
        print("one or more GET requests have failed")
        return

    json_decoder = JSONDecoder()

    employee_json = employee_get.content.decode()
    employee_dict = json_decoder.decode(employee_json)
    employee_get.close()

    tasks_json = tasks_get.content.decode()
    tasks_list = json_decoder.decode(tasks_json)
    tasks_get.close()

    username = employee_dict.get("username")

    employee_tasks = []
    for task_dict in tasks_list:
        if task_dict.get("userId") == given_id:
            employee_tasks.append(task_dict)


    json_file = open(f"{given_id}.json", mode='w')

    for task in employee_tasks:
        task.pop("userId")
        task.pop("id")
        title = task.pop("title")
        task.update({"username": username})
        task.update({"task": title})

    json.dump({given_id: employee_tasks}, json_file)
    json_file.close()


if __name__ == "__main__":
    process_request()

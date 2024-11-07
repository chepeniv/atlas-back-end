#!/usr/bin/python3
'''
a python script that uses interfaces with an api to fetch all employees and
their todo tasks, formats the found data, and writes it a .json file

- output filename: `todo_all_employees.json`
- format per user (with collapsed whitespace):
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
    employee's todo list data in  json format to a file
    '''

    users_get = requests.get(
            "https://jsonplaceholder.typicode.com/users")
    tasks_get = requests.get(
            "https://jsonplaceholder.typicode.com/todos")
    if users_get.status_code != 200 or tasks_get.status_code != 200:
        print("one or more GET requests have failed")
        return

    json_decoder = JSONDecoder()

    users_json = users_get.content.decode()
    users_list = json_decoder.decode(users_json)
    users_get.close()

    tasks_json = tasks_get.content.decode()
    tasks_list = json_decoder.decode(tasks_json)
    tasks_get.close()

    export_data = {}
    for user in users_list:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = []
        for task in tasks_list:
            if task.get("userId") == user_id:
                task.pop("id")
                task.pop("userId")
                title = task.pop("title")
                task.update({"task": title})
                task.update({"username": username})
                user_tasks.append(task)
        export_data.update({user_id: user_tasks})

    json_file = open("todo_all_employees.json", mode='w')
    json.dump(export_data, json_file)
    json_file.close()


if __name__ == "__main__":
    process_request()

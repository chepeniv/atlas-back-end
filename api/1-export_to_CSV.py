#!/usr/bin/python3
'''
an repurposed python script that uses a provided api to fetch an employee by
their id and returns the information found about their todo list progress in
the csv data format

- records all tasks owned by the given employee
- format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- output filename: `USER_ID.csv`

'''

import csv
from json.decoder import JSONDecoder
import requests
from sys import argv


# https://jsonplaceholder.typicode.com
# routes: /todos, /todos/<idnum>, /users, /users/<idnum>
# api: GET, POST, PUT, PATCH, DELETE
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

    tasks_json = tasks_get.content.decode()
    tasks_list = json_decoder.decode(tasks_json)

    employee_tasks = []
    for task_dict in tasks_list:
        if task_dict.get("userId") == given_id:
            employee_tasks.append(task_dict)

    username = employee_dict.get("username")

    csv_file = open(f"{given_id}.csv", mode='w')

    csv_writer = csv.writer(
            csv_file,
            quoting=csv.QUOTE_ALL,
            lineterminator='\n')

    for task in employee_tasks:
        csv_writer.writerow([
                task.get("userId"),
                username,
                task.get("completed"),
                task.get("title"),
                ])


if __name__ == "__main__":
    process_request()

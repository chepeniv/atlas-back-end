#!/usr/bin/python3
'''
python script that uses a provided rest api to fetch an employee by id given
and returns information about their todo list progress
'''

from json.decoder import JSONDecoder
from sys import argv
import requests


# https://jsonplaceholder.typicode.com
# routes: /todos, /todos/<idnum>, /users, /users/<idnum>
# api: GET, POST, PUT, PATCH, DELETE
def process_request():
    '''
    takes an integer representing a employee id from argv and display the found
    employee's todo list progress in the following format :
    ----
    Employee EMPLOYEE_NAME is done with task(DONE_TASK/TOTAL_TASKS):
        TASK_TITLES
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

    employee_tasks = []
    json_decoder = JSONDecoder()

    employee_json = employee_get.content.decode()
    employee_dict = json_decoder.decode(employee_json)
    tasks_json = tasks_get.content.decode()
    tasks_list = json_decoder.decode(tasks_json)
    for task_dict in tasks_list:
        if task_dict.get("userId") == given_id:
            employee_tasks.append(task_dict)

    employee_done_tasks = []
    for task in employee_tasks:
        if task.get("completed"):
            employee_done_tasks.append(task)

    total_tasks = len(employee_tasks)
    total_done_tasks = len(employee_done_tasks)

    print(f"Employee {employee_dict.get("name")} is done with tasks({total_done_tasks}/{total_tasks})")
    for task in employee_done_tasks:
        print(f"\t{task.get("title")}")


if __name__ == "__main__":
    process_request()

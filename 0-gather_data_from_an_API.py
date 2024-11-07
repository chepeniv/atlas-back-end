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
    Employee EMPLOYEE_NAME is done with
    task(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        TASK_TITLE
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

    json_decoder = JSONDecoder()

    employee_get = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{given_id}")

    if employee_get.status_code == 200:
        todos_get = requests.get(
                "https://jsonplaceholder.typicode.com/todos")
        # get bytes and convert to string
        todos_string = todos_get.content.decode()
        # convert json string to python object
        todos_list = json_decoder.decode(todos_string)
        for todo_dict in todos_list:
            if todo_dict.get("userId") == given_id:
                print(f"{todo_dict}")
    else:
        print("employee not found")


if __name__ == "__main__":
    process_request()

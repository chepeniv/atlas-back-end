#!/usr/bin/python3
'''
python script that uses a provided rest api to fetch an employee by id given
and returns information about their todo list progress

- accept an integer (employee id) as a param
- display the employee todo list progress in this format :
----
Employee EMPLOYEE_NAME is done with
task(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE
----
'''

from sys import argv
import requests
# import urllib


# https://jsonplaceholder.typicode.com
# routes: /todos, /todos/<idnum>
# api: GET, POST, PUT, PATCH, DELETE
def process_request():
    '''
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


if __name__ == "__main__":
    process_request()

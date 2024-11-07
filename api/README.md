# Atlas Backend : API

system administrators (SREs) are software engineers that manage systems

a common best practice to expose an application or dataset is to us an API.
these are the public facing parts of a codebase that allow and control
interaction with outsiders and their request to access and modify data.

here we will access employee data via and api in-order to organize and export
to different data structures

## Resources

- [youtube: holberton APIs](https://www.youtube.com/watch?v=qn08N7Zx0Lw)
- [don't program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [API](https://www.webopedia.com/definitions/api/)
- [what is an API](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [what is a REST API](https://www.sitepoint.com/rest-api/)
- [what are microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP8 styleguide](https://peps.python.org/pep-0008/)

## Objectives

- what shouldn't bash scripting be used for
- what is an API and a REST API
- what are micro-services
- what are the CSV and JSON format
- implementing pythonic name styling for package, module, class, variable,
function, and constant
- what is the significance of CamelCase in python

## Requirements

- imported libraries must be organized in alphabetical order
- use `get` to access dictionary values by key (doesn't throw an exception)
- code should not execute when imported : `if __name__ == "__main__":`

## Tasks :

### 0 - gather data from an api

write a python script that uses a provided rest api

for a given employee id, return information about their todo list progress

#### requirements

- use the `urlib` or `request` modules
- accept an integer (employee id) as a param
- display the employee todo list progress in this format :
```
employee EMPLOYEE_NAME is done with
task(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
	TASK_TITLE
```

### 1 - export to csv

extend the python script to allow exporting to the csv data format

#### requirements

- records all tasks owned by the given employee
- format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- filename: `USER_ID.csv`

### 2 - export to json

extend the python script to allow exporting to the json data format

#### requirements

- records all tasks owned by the given employee
- format (without newlines):
```json
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
```
- filename: `USER_ID.json`

### 3 - dictionary of list of dictionaries (goddammit)

extend the python script to allow exporting to the json data format

#### requirements

- records all tasks from _all_ employees
- format (without newlines):
```json
{ "USER_ID": [
	{
    "username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": "TASK_COMPLETED_STATUS"
	}, {
    "username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": "TASK_COMPLETED_STATUS"
	}, ...
]},
{ "USER_ID": [
	{
    "username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": "TASK_COMPLETED_STATUS"
	}, {
    "username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": "TASK_COMPLETED_STATUS"
	}, ...
]}...
```
- filename: `todo_all_employees.json`

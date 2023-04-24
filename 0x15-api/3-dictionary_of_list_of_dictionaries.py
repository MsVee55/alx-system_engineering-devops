#!/usr/bin/python3
'''
A Python script to export all users data in the JSON format.
'''

import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    allUsers = requests.get("{}/users".format(url)).json()
    usersDataObj = {}
    for user in allUsers:
        allTasks = requests.get(
            "{}/todos?userId={}".format(url, user.get("id"))).json()
        usersDataObj[user.get("id")] = [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in allTasks]
    with open("todo_all_employees.json", "w") as jsonFile:
        json.dump(usersDataObj, jsonFile)

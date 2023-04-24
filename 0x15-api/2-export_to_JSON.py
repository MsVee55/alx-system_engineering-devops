#!/usr/bin/python3
'''
A Python script to export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    if (len(argv) > 1):
        userId = argv[1]
        url = 'https://jsonplaceholder.typicode.com'
        userData = requests.get("{}/users/{}".format(url, userId)).json()
        userName = userData.get("name")
        if userName is not None:
            allTasks = requests.get(
                "{}/todos?userId={}".format(url, userId)).json()
            tasksList = [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": userData.get("username")
            } for task in allTasks]
        with open("{}.json".format(userId), "w") as jsonFile:
            json.dump({userId: tasksList}, jsonFile)

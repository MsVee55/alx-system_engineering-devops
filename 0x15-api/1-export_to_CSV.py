#!/usr/bin/python3
'''
A Python script to export data in CSV format.
'''
import csv
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
        with open("{}.csv".format(userId), "w") as csvFile:
            writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
            for task in allTasks:
                writer.writerow([userId, userData.get(
                    "username"), task.get("completed"), task.get("title")])

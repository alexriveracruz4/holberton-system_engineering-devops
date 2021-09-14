#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": userId}).json()

    json_dict = {}
    json_dict[userId] = [{"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": username} for task in tasks]

    with open("{}.json".format(userId), "w") as f:
        json.dump(json_dict, f)

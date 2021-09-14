#!/usr/bin/python3
"""Exports all tasks into the JSON format"""
import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    json_dict = {}

    for user in users:
        task_list = []
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id'))).json()
        for task in tasks:
            t = {}
            t["task"] = task.get("title")
            t["completed"] = task.get("completed")
            t["username"] = user.get("username")
            task_list.append(t)
        json_dict[user.get('id')] = task_list

        with open("todo_all_employees.json", "w") as f:
            json.dump(json_dict, f)

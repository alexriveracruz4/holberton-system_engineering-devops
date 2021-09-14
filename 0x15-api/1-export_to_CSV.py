#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in tasks:
            wr.writerow([userId, username, t.get("completed"), t.get("title")])

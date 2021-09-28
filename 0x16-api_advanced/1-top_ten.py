#!/usr/bin/python3
"""Request appi"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    results = resp.json().get("data").get("children")
    [print(r.get("data").get("title")) for r in results]

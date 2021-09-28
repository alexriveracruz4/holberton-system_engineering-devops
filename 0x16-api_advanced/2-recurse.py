#!/usr/bin/python3
"""Request API"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """recursive for hot post"""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-agent": "MyAPI/0.0.1"}
    params = {'after': after}

    res = requests.get(URL, headers=headers, params=params,
                       allow_redirects=False)

    if (res.status_code != 200):
        return (None)

    data = res.json()['data']
    for each in data['children']:
        hot_list.append(each['data']['title'])
    after = data['after']
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list if len(hot_list) > 0 else None

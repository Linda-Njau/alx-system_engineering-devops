#!/usr/bin/python3
"""
this script works recursively to return list of titles of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function that returns hot list of a subreddit
    """
    headers = {
        "User-Agent": "linux:myserver:v5.11.0 (by /u/linda)"
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    titles = data['data']['children']
    for title in titles:
        hot_list.append(title['data']['title'])
    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

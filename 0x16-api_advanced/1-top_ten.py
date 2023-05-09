#!/usr/bin/python3
"""
function queries for the first top ten posts of a subreddit
"""
from urllib import response
import requests


def top_ten(subreddit):
    """
    Returns the top 10 subreddit posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:myserver:v5.11.0 (by /u/linda)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data")
    children = data.get("children")
    for i in range(10):
        print(children[i].get("data").get("title"))

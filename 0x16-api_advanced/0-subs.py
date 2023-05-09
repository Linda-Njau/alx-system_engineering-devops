#!/usr/bin/python3
"""Function that queries Reddit for info on subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """function to return subscriber info"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:myserver:v5.11.0 (by /u/linda)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")

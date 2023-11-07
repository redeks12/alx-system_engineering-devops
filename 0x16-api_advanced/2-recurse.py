#!/usr/bin/python3
"""Write a function that queries the
Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Write a function that queries the
    Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit."""
    my_list = hot_list
    params = {"limit": "100"}
    if after:
        params["after"] = after
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "subscribercheck",
        },
        params=params,
        allow_redirects=False,
    )
    if response.status_code is not 200:
        return None
    resp = response.json()["data"]["children"]
    if resp:
        for i in resp:
            my_list.append(i["data"]["title"])

        afterd = response.json()["data"]["after"]
        if afterd is None:
            return my_list
        else:
            return recurse(subreddit, my_list, afterd)

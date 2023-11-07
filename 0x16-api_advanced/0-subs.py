#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "subscribercheck"},
        allow_redirects=False,
    )
    if response.status_code != 200:
        return 0
    rep = response.json()["data"]["subscribers"]
    return rep

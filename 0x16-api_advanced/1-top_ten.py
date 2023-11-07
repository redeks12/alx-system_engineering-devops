#!/usr/bin/python3
"""Write a function that queries the
Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Write a function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "subscribercheck",
        },
        params={"limit": "10"},
        allow_redirects=False,
    )
    if response.status_code != 200:
        print(None)
        return
    resp = response.json()["data"]["children"]
    for i in resp:
        print(i["data"]["title"])

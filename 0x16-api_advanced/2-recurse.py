#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], count=0):
    """Write a function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit."""
    after = None
    all_posts = []
    for i in range(10):
        params = {"limit": "10"}
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

        resp = response.json()["data"]["children"]
        for i in resp:
            all_posts.append(i["data"]["title"])

        after = response.json()["data"]["after"]
        print(after)
    # print(all_posts)


recurse("programming")


def recurse(subreddit, hot_list=[], count=0, after=None):
    # after = None
    params = {"limit": "10"}
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

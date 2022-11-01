#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'


def top_ten(subreddit):
    """Prints the top 10 hot post listed for a given subreddit"""
    try:
        endpoint = '/r/{}/hot.json?limit=10'.format(subreddit)
        headers = {"User-Agent": "Custom Agen"}
        res = requests.get(URL+endpoint,
                           headers=headers,
                           allow_redirects=False)
        children = res.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except Exception:
        print(None)

#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """Queries and returns the number of subcribers of a given subreddit"""
    try:
        endpoint = '/r/{}/about.json'.format(subreddit)
        headers = {"User-Agent": "Custom Agen"}
        res = requests.get(URL+endpoint,
                           headers=headers,
                           allow_redirects=False)
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0

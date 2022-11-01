#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'
headers = {"User-Agent": "Custom Agen"}


def recursively(uri, after=None, hot_list=[]):
    """Recursive function for the job"""
    parameters = {}
    if after:
        parameters['after'] = after
    res = requests.get(uri,
                       headers=headers,
                       allow_redirects=False,
                       params=parameters)
    if res.status_code == 200:
        children = res.json().get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        new_after = res.json().get('data').get('after')
        if new_after is not None:
            recursively(uri, new_after, hot_list)
        return hot_list


def recurse(subreddit, hot_list=[]):
    """Prints the top all hot posts listed for a given subreddit"""
    try:
        uri = URL + '/r/{}/hot.json'.format(subreddit)
        return recursively(uri)
    except Exception as e:
        print(e)

#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'
headers = {"User-Agent": "Custom Agent"}


def fetch_hot_posts(uri, after=None, hot_list=[]):
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
        next_ = res.json().get('data').get('after')
        if next_ is not None:
            fetch_hot_posts(uri, next_, hot_list)
        return hot_list


def recurse(subreddit, hot_list=[]):
    """Fetchs the top hot posts listed for a given subreddit"""
    try:
        uri = URL + '/r/{}/hot.json'.format(subreddit)
        return fetch_hot_posts(uri)
    except Exception as e:
        print(e)

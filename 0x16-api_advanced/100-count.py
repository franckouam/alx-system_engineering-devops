#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'
headers = {"User-Agent": "Custom Agent"}


def count_words(subreddit, word_list):
    """Prints a count of given keywords"""
    try:
        uri = URL + '/r/{}/hot.json'.format(subreddit)
        hot_titles = fetch_hot_posts(uri)
        pure_word_list = sanitize(word_list)
        result = dict(zip(pure_word_list, [0] * len(pure_word_list)))
        for title in hot_titles:
            for word in pure_word_list:
                occurrences = count_occurrences(word, title.split())
                if occurrences:
                    result[word] += occurrences
        result = dict(sorted(result.items()))
        for key, value in result.items():
            if value:
                print("{}: {}".format(key.lower(), value))
        return result
    except Exception as e:
        print(e)


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


def count_occurrences(word, corpus):
    """Counts occurrences of a word in a list of words"""
    word = word.lower()
    count = 0
    for w in corpus:
        if w.lower() == word:
            count += 1
    return count


def sanitize(corpus):
    pure_corpus = []
    for word in corpus:
        if count_occurrences(word, pure_corpus) == 0:
            pure_corpus.append(word)
    return pure_corpus

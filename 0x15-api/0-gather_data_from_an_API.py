#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests as re
import sys


API_URL = 'https://jsonplaceholder.typicode.com'


def get_todos(user_id):
    '''Get completed TODO of a given user'''
    todos_info = {}
    try:
        res = re.get(f'{API_URL}/users/{user_id}/todos')
        todos = res.json()
        todos_info = {'total': len(todos), 'completed': []}
        todos_info['name'] = get_username(user_id)
        for todo in todos:
            if todo.get('completed'):
                todos_info['completed'].append(todo.get('title'))
    except Exception as e:
        print(e)
    return todos_info


def get_username(user_id):
    '''Get the name of a given user'''
    name = ''
    try:
        res = re.get(f'{API_URL}/users/{user_id}')
        name = res.json().get('name')
    except Exception as e:
        print(e)
    return name


if __name__ == '__main__':
    id_ = sys.argv[1]
    todos = get_todos(id_)
    completed = todos.get('completed')
    print('Employee {} is done with tasks({}/{})'.format(
                    todos.get('name'),
                    len(completed),
                    todos.get('total')
           ))
    for c in completed:
        print('\t{}'.format(c))

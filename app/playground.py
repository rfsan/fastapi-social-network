import json
import requests


def pprint(anything):
    print(json.dumps(anything, indent=4, ensure_ascii=False))


URL = 'http://127.0.0.1:8000'
USER_1 = {'email': 'david@test.com', 'password': '12345'}
USER_2 = {'email': 'roger@test.com', 'password': '12345'}


# USERS
def create_user(email, password):
    user_credentials = {'email': email, 'password': password}
    response = requests.post(URL+'/users', json=user_credentials)
    return response


# AUTH
def get_login_token(email, password):
    user_credentials = {'username': email, 'password': password}
    response = requests.post(URL+'/login', data=user_credentials)
    return response.json()['access_token']


# POSTS
def get_post(user, id):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(URL+f'/posts/{id}', headers=headers)
    return {'STATUS_CODE': response.status_code, 'BODY': response.json()}


def create_post(user, title, content):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    body = {'title': title, 'content': content}
    response = requests.post(URL+'/posts', headers=headers, json=body)
    return {'STATUS_CODE': response.status_code, 'BODY': response.json()}


def delete_post(user, id):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(URL+f'/posts/{id}', headers=headers)
    return {'STATUS_CODE': response.status_code}


def update_post(user, id, title, content):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    body = {'title': title, 'content': content}
    response = requests.put(URL+f'/posts/{id}', headers=headers, json=body)
    return {'STATUS_CODE': response.status_code, 'BODY': response.json()}


def get_posts(user, limit=None, skip=None):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    params = {}
    if limit is not None:
        params['limit'] = limit
    if skip is not None:
        params['skip'] = skip
    response = requests.get(URL+'/posts', headers=headers, params=params)
    return {'STATUS_CODE': response.status_code, 'BODY': response.json()}


# VOTE
def vote(user, post_id, direction):
    token = get_login_token(**user)
    headers = {'Authorization': f'Bearer {token}'}
    body = {'post_id': post_id, 'direction': direction}
    response = requests.post(URL+'/vote', headers=headers, json=body)
    return {'STATUS_CODE': response.status_code, 'BODY': response.json()}


if __name__ == '__main__':
    # create_user(**USER_1)
    # create_user(**USER_2)

    pprint(get_post(USER_1, 1))
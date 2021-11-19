import json
import requests


if __name__ == '__main__':
    from generic import URL, TEST_USER, login_token
else:
    from .generic import URL, TEST_USER, login_token



# CREATE POSTS


# GET POSTS
def test_get_posts_with_correct_token():
    token = login_token(**TEST_USER)
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(URL+'/posts', headers=headers)
    assert response.status_code == 200

def test_get_posts_with_wrong_token():
    token = login_token(**TEST_USER)
    headers = {
        'Authorization': f'Bearer {token}s'
    }
    response = requests.get(URL+'/posts', headers=headers)
    assert response.status_code == 401

def test_get_posts_without_token():
    response = requests.get(URL+'/posts')
    assert response.status_code == 401


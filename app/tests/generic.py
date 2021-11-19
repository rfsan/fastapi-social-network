import requests


URL = 'http://127.0.0.1:8000'
TEST_USER = {
    'email': 'testuser@test.com',
    'password': '12345'
}


def login_token(email, password):
    user_credentials = {
        'username': email,
        'password': password
    }
    response = requests.post(URL+'/login', data=user_credentials)

    return response.json()['access_token']
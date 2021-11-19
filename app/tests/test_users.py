from datetime import datetime
import requests

if __name__ == '__main__':
    from generic import URL
else:
    from .generic import URL


def create_user(email, password):
    user_credentials = {
        'email': email,
        'password': password
    }
    r = requests.post(URL+'/users', json=user_credentials)
    return r


def test_create_user():
    now = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f')
    email, password = f'testuser{now}@test.com', '12345'
    response = create_user(email, password)
    response_body = response.json()

    assert response.status_code == 201
    assert response.headers['content-type'] == 'application/json'
    assert response_body['email'] == email
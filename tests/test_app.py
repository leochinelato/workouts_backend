from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, mundo!'}


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'string',
                'email': 'user@example.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_user_error(client):
    response = client.get('/users/111111')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'joao',
            'email': 'joao@example.com',
            'password': 'string',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'joao',
        'email': 'joao@example.com',
        'id': 1,
    }


def test_update_user_error(client):
    response = client.put(
        '/users/111',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted.'}


def test_delete_user_error(client):
    response = client.delete('/users/111')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

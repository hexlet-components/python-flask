import pytest
from hello_world import app as flask_app


@pytest.fixture()
def app():
    flask_app.config.update({
        'TESTING': True,
    })
    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hello World!' in response.text


def test_bottles(client):
    response = client.get('/99-bottles')
    assert response.status_code == 200
    assert response.text.count('<li>') == 100


def test_args(client):
    """
    a | 1 | 2
    b | 1 |
    c | 3 | 4
    """
    response = client.get('/args/?a=1&a=2&b=1&c=3&c=4')
    assert response.status_code == 200
    assert response.text.count('<tr>') == 3
    assert response.text.count('<td>') == 8


def test_json(client):
    response = client.get('/json/?a=1&a=2&b=1&c=3&c=4')
    assert response.status_code == 200
    assert response.json == {
        'a': ['1', '2'],
        'b': ['1'],
        'c': ['3', '4'],
    }  # noqa: WPS221


def test_error(client):
    with pytest.raises(ZeroDivisionError):
        client.get('/error')

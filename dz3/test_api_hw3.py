import pytest


@pytest.mark.parametrize('todo_id', [1, 200])
def test_getting_positive(session, base_url, todo_id):
    res = session.get(url=f'{base_url}/{todo_id}')

    assert res.status_code == 200
    assert res.json()['id'] == todo_id

def test_getting_negative(session, base_url, incorrect_todo_id):
    res = session.get(url=f'{base_url}/{incorrect_todo_id}')

    assert res.status_code == 404

@pytest.mark.parametrize('todo_index, expected', [(0, 1), (199, 10)])
def test_listing_all(session, base_url, todo_index, expected):
    res = session.get(url=f'{base_url}')
    json = res.json()
    todo = json[todo_index]

    assert todo['userId'] == expected
    assert res.status_code == 200


def test_creating(session, base_url):
    title = 'creating new todo!'
    completed = 'false'
    payload = {'userId': 10, 'title': title, 'completed': completed}
    res = session.post(url=f'{base_url}', json=payload)

    assert res.status_code == 201
    assert res.json()['title'] == title


def test_updating_with_put_positive(session, base_url):
    payload = {'completed': 'true'}
    res = session.put(url=f'{base_url}/1', json=payload)

    assert res.status_code == 200
    assert res.json() == {'completed': 'true', 'id': 1}


def test_updating_with_put_negative(session, base_url, incorrect_todo_id):
    payload = {'completed': 'true'}
    res = session.put(url=f'{base_url}/{incorrect_todo_id}', json=payload)

    assert res.status_code == 500


def test_updating_with_patch(session, base_url):
    payload = {'completed': 'true'}
    res = session.patch(url=f'{base_url}/1', json=payload)

    assert res.status_code == 200
    assert res.json() == {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': 'true'}


def test_deleting(session, base_url):
    res = session.delete(url=f'{base_url}/1')

    assert res.status_code == 200


def test_filtering_positive(session, base_url):
    res = session.get(url=f'{base_url}?userId=1&id=1')

    assert res.status_code == 200
    assert res.json() == [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}]


def test_filtering_negative(session, base_url):
    res = session.get(url=f'{base_url}?userId=0')

    assert res.status_code == 200
    assert res.json() == []

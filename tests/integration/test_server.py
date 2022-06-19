
def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'FizzBuzz' in response.data


def test_fizzbuzz_(test_client):
    response = test_client.post('/fizzbuzz', data=dict(fizzbuzz=10))
    assert response.status_code == 200
    assert b'fizzbuzz' not in response.data

    response = test_client.post('/fizzbuzz', data=dict(fizzbuzz=15))
    assert response.status_code == 200
    assert b'fizzbuzz' in response.data


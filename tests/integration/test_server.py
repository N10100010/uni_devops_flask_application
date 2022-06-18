
def test_ping(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'FizzBuzz' in response.data


def test_get_users(test_client):
    response = test_client.post('/fizzbuzz', )
    assert response.status_code == 200

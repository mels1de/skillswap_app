def test_register_and_login(client):
    payload = {'email': 'foo@example.com', 'password': 'some_password123'}

    resp = client.post('/auth/register', json=payload)
    assert resp.status_code == 200, resp.text
    data = resp.json()
    assert 'id' in data
    assert data['email'] == payload['email']

    resp1 = client.post(
        '/auth/login',
        data={'username': payload['email'], 'password': payload['password']}
    )
    assert resp1.status_code == 200, resp1.text
    data3 = resp1.json()
    assert 'access_token' in data3 and data3['token_type'] == 'bearer'

    headers = {'Authorization': f"Bearer {data3['access_token']}"}
    resp3 = client.get('/auth/me', headers=headers)
    assert resp3.status_code == 200, resp3.text
    assert resp3.json()['email'] == payload['email']

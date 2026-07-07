def test_register(client):

    response = client.post(
        "/auth/register",
        json={
            "name": "Admin",
            "email": "admin@gmail.com",
            "password": "admin123",
            "role": "Admin"
        }
    )

    assert response.status_code == 200


def test_login(client):

    client.post(
        "/auth/register",
        json={
            "name": "Admin",
            "email": "admin@gmail.com",
            "password": "admin123",
            "role": "Admin"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "admin@gmail.com",
            "password": "admin123"
        }
    )

    assert response.status_code == 200

    assert "access_token" in response.json()
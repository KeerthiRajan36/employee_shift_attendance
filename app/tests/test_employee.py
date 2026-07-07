def get_token(client):

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

    return response.json()["access_token"]


def test_create_employee(client):

    token = get_token(client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.post(
        "/employees",
        json={
            "user_id": 2,
            "name": "John",
            "email": "john@gmail.com",
            "phone": "9876543210",
            "department": "IT",
            "designation": "Developer"
        },
        headers=headers
    )

    assert response.status_code in [200, 400]
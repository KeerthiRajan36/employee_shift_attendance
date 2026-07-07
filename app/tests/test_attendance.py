from app.tests.test_employee import get_token


def test_get_attendance(client):

    token = get_token(client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.get(
        "/attendance",
        headers=headers
    )

    assert response.status_code == 200
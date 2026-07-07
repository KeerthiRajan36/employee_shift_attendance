from app.tests.test_employee import get_token


def test_create_shift(client):

    token = get_token(client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.post(
        "/shifts",
        json={
            "shift_name": "Morning",
            "start_time": "09:00:00",
            "end_time": "18:00:00",
            "shift_type": "General"
        },
        headers=headers
    )

    assert response.status_code == 200
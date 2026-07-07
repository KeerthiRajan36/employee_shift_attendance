from app.tests.test_employee import get_token


def test_monthly_report(client):

    token = get_token(client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.get(
        "/reports/monthly?month=7&year=2026",
        headers=headers
    )

    assert response.status_code == 200
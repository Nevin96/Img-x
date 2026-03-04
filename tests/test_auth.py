import uuid

def test_register(client):
    email = f"test_{uuid.uuid4()}@example.com"
    response = client.post(
        "/auth/register",
        json={
            "email":email,
            "password":"password123"
        }
    )

    assert response.status_code == 201

def test_login(client):
    client.post(
        "/auth/register",
        json={
            "email":"test@example.com",
            "password":"password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email":"test@example.com",
            "password":"password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
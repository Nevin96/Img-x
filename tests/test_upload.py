def get_token(client):
    client.post(
        "/auth/register",
        json={
            "email": "upload@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "upload@example.com",
            "password": "password123"
        }
    )
    return response.json()["access_token"]

def test_upload(client):
    token = get_token(client)
    headers = {
        "Authorization" : f"Bearer {token}"
    }

    with open("tests/sample.jpg",'rb') as f:
        response = client.post(
            "/images/upload",
            files = {"file":("sample.jpg",f,"image/jpeg")},
            headers= headers
        )
    assert response.status_code in (200,201)
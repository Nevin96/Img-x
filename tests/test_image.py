def test_list_images(client):
    response = client.get("/images?page=1&limit=5")

    assert response.status_code in (200,401)
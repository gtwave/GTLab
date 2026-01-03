from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_extract_chords():
    response = client.post("/extract_chords", json={"url": "https://youtube.com/example"})
    assert response.status_code == 200
    data = response.json()
    assert "chords" in data
    assert isinstance(data["chords"], list)

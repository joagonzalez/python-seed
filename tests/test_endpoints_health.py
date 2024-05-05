from src import app
from fastapi.testclient import TestClient



client = TestClient(app=app)


def test_read_main():
    response: TestClient = client.get("/health/status/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
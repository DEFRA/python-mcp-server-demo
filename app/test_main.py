from fastapi.testclient import TestClient

from .entrypoints.http.main import api

client = TestClient(api)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 404

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_imports_and_root():
    # basic smoke test to ensure pytest is running and app is importable
    response = client.get("/")
    assert response.status_code == 200

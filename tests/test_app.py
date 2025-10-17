import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup", params={"email": "testuser@example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up testuser@example.com for Chess Club"


def test_signup_for_nonexistent_activity():
    response = client.post("/activities/Nonexistent/signup", params={"email": "testuser@example.com"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_from_activity():
    response = client.delete("/activities/Chess Club/unregister", params={"email": "daniel@mergington.edu"})
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered daniel@mergington.edu from Chess Club"


def test_unregister_from_nonexistent_activity():
    response = client.delete("/activities/Nonexistent/unregister", params={"email": "testuser@example.com"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
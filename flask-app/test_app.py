import pytest
from app import app # Replace 'app' with the name of your python file

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    app.config.update({"TESTING": True})
    
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Tests the root endpoint returns correct JSON and 200 status."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Flask app running inside Docker 🚀"}

def test_health_route(client):
    """Tests the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_404_route(client):
    """Tests that a non-existent route returns a 404."""
    response = client.get("/not-real")
    assert response.status_code == 404
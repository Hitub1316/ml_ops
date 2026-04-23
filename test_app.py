import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Classification API is running"}

def test_predict(client):
    """Test the predict route."""
    response = client.post('/predict', json={"val": 1.0})
    assert response.status_code == 200
    data = response.get_json()
    assert data["input"] == 1.0
    assert "prediction" in data

def test_predict_invalid(client):
    """Test the predict route with invalid data."""
    response = client.post('/predict', json={})
    assert response.status_code == 400
# test_app.py
import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_predict():
    client = app.test_client()
    response = client.post('/predict', json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
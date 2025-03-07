# What to test:
# 1. Error cases
#   - API keys not found
#   - Invalid city name
# 2. API calls
#    - return correct data
# 3. UI
# 4. Input
# 5. Output
# API keys
# / return HTTP 200

import pytest

from app import app

def test_landing_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Enter a location" in response.data
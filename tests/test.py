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
import os

from app import app

def test_landing_page_returns_200_and_placeholder_found_from_response():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Enter a location" in response.data

def test_landing_page_returns_error_if_owm_api_key_not_found():
    with app.test_client() as client:
        app.api_key_owm = os.getenv("OWM_API_KE")
        response = client.get('/')
        assert response.status_code == 404
        assert b"Error: API key not found. Set OWM_API_KEY in your .env file." in response.data

def test_landing_page_returns_error_if_wa_api_key_not_found():
    with app.test_client() as client:
        app.api_key_owm = os.getenv("OWM_API_KE")
        response = client.get('/')
        assert response.status_code == 404
        assert b"Error: API key not found. Set WA_API_KEY in your .env file." in response.data
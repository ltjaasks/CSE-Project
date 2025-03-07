import pytest
from app import app, get_temperature_from_api
import requests
import requests_mock
from unittest.mock import patch
# What to test:
# 1. Error cases
# 2. API calls
# 3. UI
# 4. Input
# 5. Output
# API keys

def test_landing_page_returns_200_and_placeholder_found_from_response():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Enter a location" in response.data

@patch('requests.get')
def test_invalid_city_name_raises_value_error(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.json_return_value = {
        "cod":"404",
        "message":"city not found"
        }
    
    url = 'http://example.com/api'

    with pytest.raises(ValueError):
        get_temperature_from_api(url)
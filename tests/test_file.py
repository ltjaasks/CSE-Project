import pytest
from app import app, get_temperature_from_api
import requests
import requests_mock
from unittest.mock import patch
import os

from app import app



def test_landing_page_returns_200_and_placeholder_found_from_response():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Enter a location" in response.data


# Error tests
@patch('requests.get')
def test_invalid_city_name_raises_value_error(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.json_return_value = {
        "cod":"404",
        "message":"city not found"
        }

    with pytest.raises(ValueError, match="Enter a valid city name"):
        get_temperature_from_api('http://example.com/api')


def test_error_is_raised_and_weather_info_not_returned_if_invalid_city_name():
    with app.test_client() as client:
        response = client.post('/', data={'location': 'fakeCityName'})
        assert response.status_code == 404
        assert b"Enter a valid city name" in response.data


# API tests
def test_landing_page_returns_error_if_owm_api_key_not_found(monkeypatch: pytest.MonkeyPatch):
    def get_api_keys(): return None, os.getenv("WA_API_KEY")
    monkeypatch.setattr("app.get_api_keys", get_api_keys)
    with app.test_client() as client:
        app.api_key_owm = os.getenv("OWM")
        print("OWM-key", app.api_key_owm)
        response = client.get('/')
        assert response.status_code == 404


def test_landing_page_returns_error_if_wa_api_key_not_found(monkeypatch: pytest.MonkeyPatch):
    def get_api_keys(): return os.getenv("OWM_API_KEY"), None
    monkeypatch.setattr("app.get_api_keys", get_api_keys)
    with app.test_client() as client:
        app.api_key_wa = os.getenv("WA")
        response = client.get('/')
        assert response.status_code == 404

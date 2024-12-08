import requests
import pytest
from unittest.mock import patch

def test_unauthorized_access(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""

    with patch('requests.get', return_value=mock_response):
        response = requests.get(url, params=params)
    
    assert response.status_code == 401
    assert response.text == ""

def test_authorized_access(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""

    with patch('requests.get', return_value=mock_response):
        response = requests.get(url, params=params)
    
    assert response.status_code == 200
    assert response.text == ""

if __name__ == "__main__":
    pytest.main()
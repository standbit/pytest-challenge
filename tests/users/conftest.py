import pytest
import requests
import json


SERVICE_URL="https://gorest.co.in/public/v1/users"

@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response

@pytest.fixture
def get_content():
    with open('./regular_users.json', 'r') as read_file:
        content = json.load(read_file)
    return content
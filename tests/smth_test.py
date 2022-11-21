import requests
from configurations import SERVICE_URL
from src.enums.global_enums import GloballErrorMessages


def test_get_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GloballErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GloballErrorMessages.WRONG_ELEMENT_COUNT.value
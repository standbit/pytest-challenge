import requests

from configurations import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA

r = requests.get(url=SERVICE_URL)
response = Response(r)


def test_get_posts():
    response.check_status_code(200).validate(POST_SCHEMA)

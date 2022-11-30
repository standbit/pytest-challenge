import requests
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User

SERVICE_URL="https://gorest.co.in/public/v1/users"


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_obj = Response(response)
    test_obj.assert_status_code(200).validate(User)

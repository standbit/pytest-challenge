import pytest

from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)

@pytest.mark.production
@pytest.mark.skip("not needed yes")
def test_another():
    assert 1 == 1

@pytest.mark.development
@pytest.mark.parametrize('first_val, second_val, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    (-1, 'b', None),
    ('a', 'b', None),
])
def test_calculator(first_val, second_val, result, calculate):
    assert calculate(first_val, second_val) == result
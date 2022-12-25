import pytest

from src.baseclasses.response import Response, Content
from src.pydantic_schemas.user import User, TestUser


def test_getting_users_list(get_users):
    '''
    In this test we check, that http code is ok and response corresponds to schema
    '''
    Response(get_users).assert_status_code(200).validate(User)


def test_user_schema(get_content):
    '''
    In this test json scheme from a1qa is tested
    '''
    Content(get_content).validate(TestUser)


def test_address(get_content):
    '''
    In this test we check that address field is not empty
    '''
    con = Content(get_content)
    for item in con.content:
        assert len(item["address"]) != 0, f"Error here-> id: {item['id'], 'address is: ', item['address']}"


@pytest.mark.production
@pytest.mark.skip("not needed yet")
def test_another():
    '''
    In this test we check, that 1 is equal to 1
    '''
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
    '''
    In this test we are testing calculation of two values (valid and invalid)
    '''
    assert calculate(first_val, second_val) == result

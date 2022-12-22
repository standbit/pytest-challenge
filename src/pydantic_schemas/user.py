from pydantic import BaseModel, validator

from src.enums.user_enums import Genders, Statuses, UserErrors

class Address(BaseModel):
    city: str
    street: str
    building: int


class TestUser(BaseModel):
    id: int
    name: str
    address: dict

    @validator('address')
    def check_address_is_nit_empty(cls, address):
        if address:
            return address
        else:
            return ValueError(UserErrors.WRONG_ADDRESS.value)


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email(cls, email):
        if '@' in email:
            return email
        else:
            return ValueError(UserErrors.WRONG_EMAIL.value)

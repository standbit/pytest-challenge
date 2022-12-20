import pytest
from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 100, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    # print("I'm getting number")
    number = randrange(1, 1000, 55)
    #передача потока - управления
    yield number
    # print(f"Number at home {number}")
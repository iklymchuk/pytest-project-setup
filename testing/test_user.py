# from ..src.user import random_user
from src.user import random_user


def test_random_user():
    assert "guest" or "regular" or "admin" in random_user()

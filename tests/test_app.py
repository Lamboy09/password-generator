import pytest
import string

from app import password_generator

chars: str = string.ascii_lowercase + string.ascii_uppercase


def test_password_generator():
    password = password_generator(5, 5, 5)
    assert password
    assert type(password) == str
    assert len(password) == 15
    assert sum(1 for c in password if c in chars) == 5

    password = password_generator(1, 2, 3)
    assert password
    assert len(password) == 6
    assert sum(1 for c in password if c in chars) == 1

    password = password_generator(0, 1, 3)
    assert password
    assert len(password) == 4
    assert sum(1 for c in password if c in chars) == 0

    # NOTE Revisit to fix in app.py, once done remove not
    password = password_generator(0, 0, 0)
    assert not password
    assert len(password) == 0


def test_password_generator_breaks():
    with pytest.raises(TypeError) as e:
        password = password_generator(5, 5, "a")
        assert e.message == "'str' object cannot be interpreted as an integer"

    password = password_generator(-5, -5, -5)
    assert not password
    assert len(password) == 0

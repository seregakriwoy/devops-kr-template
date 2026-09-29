# tests/test_validator.py
from validator import validate_phone


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+799912345678") == False
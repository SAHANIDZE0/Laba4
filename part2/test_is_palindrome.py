import pytest
from is_palindrome import is_palindrome

@pytest.mark.parametrize("value, expected", [
    ("Шалаш", True),
    ("А роза упала на лапу Азора", False), 
    ("Madam", True),
    ("hello", False),
    (12321, True),
    (12345, False),
    ("", True),
    ("A", True)
])
def test_is_palindrome(value, expected):
    assert is_palindrome(value) == expected
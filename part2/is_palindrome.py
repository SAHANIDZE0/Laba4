def is_palindrome(value):
    """Принимает строку или целое число, возвращает True, если это палиндром, иначе False."""
    s = str(value).lower()
    return s == s[::-1]
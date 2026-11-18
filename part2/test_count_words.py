import pytest
from count_words import count_words

@pytest.mark.parametrize("sentence, expected", [
    ("Привет мир", 2),
    ("  Много   пробелов   здесь ", 3),
    ("", 0),
    ("   ", 0),
    ("Одно", 1),
    ("Знаки препинания, и запятые.", 4)
])
def test_count_words(sentence, expected):
    assert count_words(sentence) == expected
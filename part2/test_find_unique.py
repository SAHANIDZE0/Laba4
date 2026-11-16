import pytest
from find_unique import find_unique

@pytest.mark.parametrize("items, expected", [
    ([1, 2, 2, 3, 3, 3], [1]),
    (['a', 'b', 'a', 'c', 'b'], ['c']),
    ([1, 1, 1], []),
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 5, 4, 4, 3], [3])
])
def test_find_unique(items, expected):
    assert find_unique(items) == expected
import pytest
from combine_dicts import combine_dicts

@pytest.mark.parametrize("d1, d2, expected", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 1, 'b': 3, 'c': 4}),
    ({}, {'a': 1}, {'a': 1}),
    ({'a': 1}, {}, {'a': 1}),
    ({}, {}, {}),
    ({'x': 10}, {'x': 20}, {'x': 20})
])
def test_combine_dicts(d1, d2, expected):
    assert combine_dicts(d1, d2) == expected

def test_combine_dicts_immutable():
    d1 = {'a': 1}
    d2 = {'b': 2}
    combine_dicts(d1, d2)
    assert d1 == {'a': 1}
    assert d2 == {'b': 2}
import pytest
from foo_bar_baz import foo_bar_baz

"""
Lists every number from 1 to n.
Replaces numbers divisible by 3 with "Foo".
Replaces numbers divisible by 5 with "Bar".
Replaces numbers divisible by both 3 and 5 with "Baz".
"""

add_cases = [
    (-1, ""),
    (0, ""),
    (1, "1"),
    (2, "1 2"),
    (3, "1 2 Foo"),
    (5, "1 2 Foo 4 Bar"),
    (16, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16"),
]


@pytest.mark.parametrize("n, result", add_cases)
def test_test(n, result):
    assert foo_bar_baz(n) == result and is_space_delimited_string(n)


def is_space_delimited_string(n: int):
    return isinstance(foo_bar_baz(n), str) and is_valid_string(foo_bar_baz(n))


def is_valid_string(string: str):
    list = string.split()
    for element in list:
        if len(element) > 1 and not element.isdigit() and not element.isalpha():
            return False
    return True

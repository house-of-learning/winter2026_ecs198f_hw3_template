import pytest
from foo_bar_baz import foo_bar_baz

"""
Lists every number from 1 to n.
Replaces numbers divisible by 3 with "Foo".
Replaces numbers divisible by 5 with "Bar".
Replaces numbers divisible by both 3 and 5 with "Baz".
"""

test_cases = [
    # Edge cases
    (-1, ""),
    (0, ""),

    # Basic cases
    (1, "1"),
    (2, "1 2"),

    # Divisible by 3 (Foo)
    (3, "1 2 Foo"),
    (6, "1 2 Foo 4 Bar Foo"),
    (9, "1 2 Foo 4 Bar Foo 7 8 Foo"),

    # Divisible by 5 (Bar)
    (5, "1 2 Foo 4 Bar"),
    (10, "1 2 Foo 4 Bar Foo 7 8 Foo Bar"),

    # Divisible by both 3 and 5 (Baz)
    (15, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"),
    (16, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16"),

    # Big sequence
    (30, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"),
]


@pytest.mark.parametrize("n, expected", test_cases)
def test_foo_bar_baz_output(n, expected):
    """Test that foo_bar_baz produces the correct output for given input."""
    actual = foo_bar_baz(n)
    assert actual == expected, f"For n={n}, expected '{expected}', but got '{actual}'"


@pytest.mark.parametrize("n, expected", test_cases)
def test_foo_bar_baz_format(n, expected):
    actual = foo_bar_baz(n)

    # Check if string
    assert isinstance(actual, str), f"Expected string, got {type(actual)}"

    # Check proper format
    assert is_properly_formatted(actual), f"String '{actual}' is not properly formatted"

    # Check elements are valid
    assert has_valid_elements(actual), f"String '{actual}' contains invalid elements"


def is_properly_formatted(s: str) -> bool:
    if not s:
        return True

    # Check for leading or trailing spaces
    if s != s.strip():
        return False

    # Check for double spaces
    if "  " in s:
        return False

    return True


def has_valid_elements(s: str) -> bool:
    if not s:
        return True

    elements = s.split()
    valid_keywords = {"Foo", "Bar", "Baz"}

    for element in elements:
        if element in valid_keywords:
            continue

        # Check if it's a positive integer
        if element.isdigit() and int(element) > 0:
            continue

        return False

    return True


def test_divisibility_rules():
    result = foo_bar_baz(15)
    elements = result.split()

    assert elements[2] == "Foo", "Number 3 should be replaced with 'Foo'"

    assert elements[4] == "Bar", "Number 5 should be replaced with 'Bar'"

    assert elements[5] == "Foo", "Number 6 should be replaced with 'Foo'"

    assert elements[14] == "Baz", "Number 15 should be replaced with 'Baz'"


def test_sequential_order():
    result = foo_bar_baz(20)
    elements = result.split()

    position = 1
    for element in elements:
        if element.isdigit():
            assert int(element) == position, f"Expected number {position}, got {element}"
        position += 1

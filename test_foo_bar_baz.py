import pytest
from foo_bar_baz import foo_bar_baz

"""
Lists every number from 1 to n.
Replaces numbers divisible by 3 with "Foo".
Replaces numbers divisible by 5 with "Bar".
Replaces numbers divisible by both 3 and 5 with "Baz".
"""


def generate_expected_output(n: int) -> str:
    if n <= 0:
        return ""

    result = []
    for i in range(1, n + 1):
        # Check divisibility by both 3 and 5 FIRST (order matters!)
        if i % 3 == 0 and i % 5 == 0:
            result.append("Baz")
        elif i % 3 == 0:
            result.append("Foo")
        elif i % 5 == 0:
            result.append("Bar")
        else:
            result.append(str(i))

    return " ".join(result)


test_values = [
    -5, -1, 0, 1, 2, 3, 4, 5, 6, 9, 10, 15, 16, 20, 30, 45, 100
]


@pytest.mark.parametrize("n", test_values)
def test_foo_bar_baz_against_spec(n):
    """Test that foo_bar_baz produces output matching the specification."""
    expected = generate_expected_output(n)
    actual = foo_bar_baz(n)
    assert actual == expected, (
        f"For n={n}:\n"
        f"Expected: '{expected}'\n"
        f"Got:      '{actual}'"
    )


@pytest.mark.parametrize("n", test_values)
def test_return_type(n):
    """Test that foo_bar_baz returns a string."""
    result = foo_bar_baz(n)
    assert isinstance(result, str), f"Expected str, got {type(result).__name__}"


@pytest.mark.parametrize("n", test_values)
def test_string_formatting(n):
    """Test that the output is properly formatted (space-delimited, no extra spaces)."""
    result = foo_bar_baz(n)

    if n <= 0:
        assert result == "", f"For n={n}, expected empty string, got '{result}'"
        return

    assert result == result.strip(), f"Result has leading/trailing spaces: '{result}'"

    assert "  " not in result, f"Result contains double spaces: '{result}'"

    elements = result.split(" ")
    assert len(elements) == n, f"Expected {n} elements, got {len(elements)}"


@pytest.mark.parametrize("n", [3, 6, 9, 12, 18])
def test_divisible_by_3(n):
    """Test that numbers divisible by only 3 are replaced with 'Foo'."""
    result = foo_bar_baz(n)
    elements = result.split()

    if n % 5 != 0:
        assert elements[n - 1] == "Foo", (
            f"Position {n} should be 'Foo' (divisible by 3), "
            f"but got '{elements[n - 1]}'"
        )


@pytest.mark.parametrize("n", [5, 10, 20, 25])
def test_divisible_by_5(n):
    """Test that numbers divisible by only 5 are replaced with 'Bar'."""
    result = foo_bar_baz(n)
    elements = result.split()

    if n % 3 != 0:
        assert elements[n - 1] == "Bar", (
            f"Position {n} should be 'Bar' (divisible by 5), "
            f"but got '{elements[n - 1]}'"
        )


@pytest.mark.parametrize("n", [15, 30, 45, 60])
def test_divisible_by_both_3_and_5(n):
    """Test that numbers divisible by both 3 and 5 are replaced with 'Baz'."""
    result = foo_bar_baz(n)
    elements = result.split()

    assert elements[n - 1] == "Baz", (
        f"Position {n} should be 'Baz' (divisible by both 3 and 5), "
        f"but got '{elements[n - 1]}'"
    )


def test_edge_case_negative():
    """Test that negative numbers return empty string."""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-100) == ""


def test_edge_case_zero():
    """Test that zero returns empty string."""
    assert foo_bar_baz(0) == ""


def test_all_elements_valid():
    """Test that all elements are either numbers, 'Foo', 'Bar', or 'Baz'."""
    result = foo_bar_baz(30)
    elements = result.split()
    valid_keywords = {"Foo", "Bar", "Baz"}

    for i, element in enumerate(elements, start=1):
        is_valid = (
            element in valid_keywords or
            (element.isdigit() and int(element) == i)
        )
        assert is_valid, (
            f"Position {i}: Invalid element '{element}'. "
            f"Expected either {i}, 'Foo', 'Bar', or 'Baz'"
        )


def test_sequential_positions():
    """Test that elements appear in sequential positions (1 to n)."""
    n = 20
    result = foo_bar_baz(n)
    elements = result.split()

    assert len(elements) == n, f"Expected {n} elements, got {len(elements)}"

    for position, element in enumerate(elements, start=1):
        if element.isdigit():
            assert int(element) == position, (
                f"At position {position}, expected number {position}, "
                f"but got {element}"
            )


def test_baz_takes_precedence_over_foo_and_bar():
    """
    Test that numbers divisible by both 3 and 5 are 'Baz', not 'Foo' or 'Bar'.
    """
    result = foo_bar_baz(15)
    elements = result.split()

    assert elements[14] == "Baz", (
        "Number 15 is divisible by both 3 and 5, should be 'Baz', "
        f"got '{elements[14]}'"
    )

    result_30 = foo_bar_baz(30)
    elements_30 = result_30.split()

    assert elements_30[29] == "Baz", (
        "Number 30 is divisible by both 3 and 5, should be 'Baz', "
        f"got '{elements_30[29]}'"
    )


def test_no_off_by_one_errors():
    """Test that the sequence includes all numbers from 1 to n (inclusive)."""
    assert foo_bar_baz(1) == "1"

    # Test that n=5 ends with "Bar" (not missing the last element)
    result_5 = foo_bar_baz(5)
    elements_5 = result_5.split()
    assert len(elements_5) == 5, "Should have exactly 5 elements"
    assert elements_5[-1] == "Bar", "Last element should be 'Bar' (for 5)"

    # Test that n=15 ends with "Baz"
    result_15 = foo_bar_baz(15)
    elements_15 = result_15.split()
    assert len(elements_15) == 15, "Should have exactly 15 elements"
    assert elements_15[-1] == "Baz", "Last element should be 'Baz' (for 15)"

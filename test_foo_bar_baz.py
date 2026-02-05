import pytest
from foo_bar_baz import foo_bar_baz
import inspect

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
    actual = foo_bar_baz(n)
    assert actual == result and is_space_delimited_string(actual)


def is_space_delimited_string(result: str):
    return isinstance(result, str) and is_valid_string(result)


def is_valid_string(string: str):
    list = string.split()
    for element in list:
        if len(element) > 1 and not element.isdigit() and not element.isalpha():
            return False
    return True


def test_function_exists():
    """Test that foo_bar_baz function exists and is callable."""
    assert callable(foo_bar_baz), "foo_bar_baz should be callable"
    assert hasattr(foo_bar_baz, '__name__'), "foo_bar_baz should have a __name__ attribute"
    assert foo_bar_baz.__name__ == 'foo_bar_baz', f"Function name should be 'foo_bar_baz', got '{foo_bar_baz.__name__}'"


def test_function_signature():
    """Test that foo_bar_baz has the correct signature."""
    sig = inspect.signature(foo_bar_baz)
    params = list(sig.parameters.keys())

    assert len(params) >= 1, "foo_bar_baz should accept at least one parameter"
    assert sig.return_annotation is str or str(sig.return_annotation) == 'str', \
        "foo_bar_baz should return a string"


def test_function_accepts_int():
    """Test that foo_bar_baz accepts integer input."""
    try:
        result = foo_bar_baz(1)
        assert isinstance(result, str), "foo_bar_baz should return a string"
    except TypeError:
        pytest.fail("foo_bar_baz should accept an integer parameter")


def test_function_returns_string():
    """Test that foo_bar_baz always returns a string type."""
    test_inputs = [-1, 0, 1, 5, 10, 15, 100]
    for n in test_inputs:
        result = foo_bar_baz(n)
        assert isinstance(result, str), f"foo_bar_baz({n}) should return str, got {type(result).__name__}"


def test_module_import():
    """Test that the module can be imported and contains foo_bar_baz."""
    import foo_bar_baz as module
    assert hasattr(module, 'foo_bar_baz'), "Module should contain 'foo_bar_baz' function"
    assert module.foo_bar_baz is foo_bar_baz, "Imported function should match"

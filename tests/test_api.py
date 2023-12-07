"""Tests for the API module."""

import pytest

from txtstats import text_stats


def test_text_stats_output_type(data_to_test):
    """Test text_stats() function for expected output type."""
    d = text_stats(data_to_test[0])

    # Check that d is a dictionary
    assert isinstance(d, dict)
    # Check that all keys in d are of type string
    assert {type(k) for k in d} == {str}


@pytest.mark.parametrize(
    "input_val, expected_error",
    [
        (1, TypeError),
        (1.34, TypeError),
        (["hello", "world"], TypeError),
        (("hello", "world", 1, 2, 3), TypeError),
    ],
)
def test_text_stats_errors(input_val, expected_error):
    """Test text_stats() function for expected errors."""
    with pytest.raises(expected_error):
        text_stats(input_val)

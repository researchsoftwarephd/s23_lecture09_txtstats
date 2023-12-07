"""Tests for the stats_functions module."""

from txtstats.stats_functions import _char_count, _line_count, _word_count


def test_char_count_result(data_to_test):
    """Test the _char_count function."""
    assert _char_count(data_to_test[0]) == data_to_test[1]["char_count"]


def test_line_count_result(data_to_test):
    """Test the _line_count function."""
    assert _line_count(data_to_test[0]) == data_to_test[1]["line_count"]


def test_word_count_result(data_to_test):
    """Test the _word_count function."""
    assert _word_count(data_to_test[0]) == data_to_test[1]["word_count"]

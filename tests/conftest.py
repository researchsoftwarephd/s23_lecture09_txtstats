"""Centralized tests configurations and fixtures."""

import pytest


@pytest.fixture(
    params=[
        ("Hello world!", {"char_count": 12, "line_count": 1, "word_count": 2}),
        ("Various\nlines\n!", {"char_count": 15, "line_count": 3, "word_count": 3}),
        ("", {"char_count": 0, "line_count": 1, "word_count": 0}),
    ]
)
def data_to_test(request):
    """Fixture that defines the data to be tested."""
    return request.param

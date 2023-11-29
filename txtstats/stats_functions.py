"""
Functions for calculating text statistics.
"""

from typing import Any


def text_stats(s: str) -> dict[str, Any]:
    """Generates statistics for the specified text.

    Args:
      s:
        The *text* from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """

    return {
        _word_count.__name__[1:]: _word_count(s),
        _line_count.__name__[1:]: _line_count(s),
        _char_count.__name__[1:]: _char_count(s),
    }


def _word_count(txt: str) -> int:
    return len(txt.split())

def _line_count(txt: str) -> int:
    return len(txt.split("\n"))

def _char_count(txt: str) -> int:
    return len(txt)
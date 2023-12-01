"""Module contains public API functions."""

from typing import Any

from .stats_finder import _find_stats


def text_stats(txt: str) -> dict[str, Any]:
    """Generate statistics for the specified text.

    Args:
      txt:
        The text from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """
    return {name: stat_func(txt) for name, stat_func in _find_stats().items()}

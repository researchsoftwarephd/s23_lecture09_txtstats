from typing import Any

from .stats_finder import _find_stats


def text_stats(s: str) -> dict[str, Any]:
    """Generates statistics for the specified text.

    Args:
      s:
        The *text* from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """

    return {name: stat_func(s) for name, stat_func in _find_stats().items()}

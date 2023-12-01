"""Contains functionality to find text statistics functions as plugins."""

import sys
from typing import Any, Callable


def _find_stats() -> dict[str, Callable[[str], Any]]:
    """Find text statistic functions registered as plugins.

    Returns:
      A dictionary containing the found text statistics functions.
    """
    if sys.version_info < (3, 10):
        from importlib_metadata import entry_points
    else:
        from importlib.metadata import entry_points

    plugin_entrypoints = entry_points(group="txtstats.stats")

    return {ep.name: ep.load() for ep in plugin_entrypoints}

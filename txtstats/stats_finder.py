from importlib.metadata import entry_points
from typing import Any, Callable


def _find_stats() -> dict[str, Callable[[str], Any]]:
    plugin_entrypoints = entry_points(group="txtstats.stats")

    return {ep.name: ep.load() for ep in plugin_entrypoints}

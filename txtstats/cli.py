import sys
from inspect import getdoc

from tabulate import tabulate

from .api import text_stats
from .stats_finder import _find_stats


def _main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as text_file:
            f_stats = text_stats(text_file.read())
        print(
            tabulate(
                f_stats.items(),
                headers=["Statistic", "Value"],
                tablefmt="rounded_outline",
            )
        )
    else:
        stats_found = _find_stats()

        stats_help = {n: getdoc(f).split("\n")[0] for n, f in stats_found.items()}

        print(
            tabulate(
                stats_help.items(),
                headers=["Statistic", "Description"],
                tablefmt="rounded_outline",
            )
        )

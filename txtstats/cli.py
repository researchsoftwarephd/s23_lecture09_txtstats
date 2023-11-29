import sys
from inspect import getdoc
from .api import text_stats
from .stats_finder import _find_stats

def _main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as text_file:
            f_stats = text_stats(text_file.read())
        for stat_name in f_stats:
            print(f"{stat_name} : {f_stats[stat_name]}")
    else:
        stats_found = _find_stats()
        for stat_name in stats_found:
            print(stat_name, " - ", getdoc(stats_found[stat_name]).split("\n")[0])
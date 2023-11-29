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

    wc = len(s.split())
    lc = len(s.split("\n"))
    cc = len(s)

    return {"word_count": wc, "line_count": lc, "char_count": cc}


if __name__ == "__main__":
    print(text_stats("Hello everyone!\nBye now!"))

"""Functions for generating text statistics."""


def _word_count(txt: str) -> int:
    """Determine the word count.

    Args:
      s:
        The text from which to obtain the word count.

    Returns:
      The word count of the specified text.
    """
    return len(txt.split())


def _line_count(txt: str) -> int:
    """Determine the line count.

    Args:
      s:
        The text from which to obtain the line count.

    Returns:
      The line count of the specified text.
    """
    return len(txt.split("\n"))


def _char_count(txt: str) -> int:
    """Determine the character count.

    Args:
      s:
        The text from which to obtain the character count.

    Returns:
      The character count of the specified text.
    """
    return len(txt)

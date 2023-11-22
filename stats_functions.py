from typing import Any

def text_stats(s: str) -> dict[str, Any]:

    wc = len(s.split())
    lc = len(s.split('\n'))
    cc = len(s)

    return {'word_count': wc, 'line_count': lc, 'char_count': cc}
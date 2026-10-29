"""Prints the law of Burkina Faso as it stood on a given day, read from this repository's history.

    python tools/en_vigueur_au.py 2020-01-01 constitution 37         # art. 37 of the Constitution on 1 January 2020
    python tools/en_vigueur_au.py 2020-01-01 constitution art-037    # the same, by file name
    python tools/en_vigueur_au.py 2020-01-01 constitution 160.1      # art. 160.1
    python tools/en_vigueur_au.py 2020-01-01 constitution            # the whole Constitution on 1 January 2020
    python tools/en_vigueur_au.py --law 2020-01-01 constitution 37   # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. A bare article number (`37`, `160.1`, `premier`) means the file
`art-037`, `art-160-1` or `art-001`. Standard library only.
"""
import re
import runpy
import sys
from pathlib import Path


def article(unit: str) -> str:
    if unit.lower() in ('premier', '1er'):
        return 'art-001'
    m = re.fullmatch(r'(\d+)(?:[.-](\d+))?', unit)
    if not m:
        return unit
    return f'art-{int(m.group(1)):03d}' + (f'-{int(m.group(2))}' if m.group(2) else '')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')

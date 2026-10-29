# How this repository was made (Burkina Faso)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| LegiBurkina (Secrétariat général du Gouvernement et du Conseil des ministres, SGG-CM/DSI) | <https://www.legiburkina.gov.bf/textesFondamentaux> | 2026-10-29 | 5 | Official text. The portal states "SGGCM/DSI @2025 - Tous droits réservés" for the site and no licence for the legal texts. |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution du Burkina Faso | 1 | 2015-11-26 to 2015-11-26 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 9 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Africa/Ouagadougou) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied as a general rule. The one version is dated by the promulgation decree of the last revision it contains, Décret n°2015-1396/PRES-TRANS du 26 novembre 2015, as listed on the consolidation itself; the date of its Journal officiel publication was not found. https://www.legiburkina.gov.bf/documents/b157d74c-23a1-4025-a8d6-0061e83df0c2/download

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/burkina-faso-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `256c871e0357256716e0c6aba2be3e59420602c2e6769a2454f3f9e3b2849d3b` (89151 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `23709bf80c349765eb453326aa9932045f37f741` |
| parse.py | `6d866f2312062eda0fa382ae71b9d151ad348e34` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 1 history commits and 1 tags (history tip `43cf785532a1ad32b7e8f0543bab12420ff66ed8`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Only the Constitution is built, on the preview branch: its current text cannot be shown. Loi constitutionnelle n°045-2023/ALT (Assemblée législative de transition, text layer) has no sourced promulgation date (the Assemblée's list says 01/01/1900); n°033-2024/ALT (promulgated 21/11/2024 per the Assemblée's list) and n°004-2026/ALT du 20 janvier 2026 are published only as scans, and scans are not transcribed (no OCR).
- One version, from 2015-11-26: the promulgation of the last revision the consolidation contains (Décret n°2015-1396/PRES-TRANS), as listed on its cover. It is credited to the publisher as the oldest version available, naming the 1991 Constitution and the eight revision laws the cover lists.
- Footnotes (9.8 pt) and footnote markers (6-9 pt superscripts) are left out; the cover page (revision and decree lists) is not law text and is left out.
- Paragraphs are rebuilt from the justified layout: a sentence end followed by a vertical gap, or by a line short of the right margin, ends a paragraph; a line without a sentence end runs on, also across a page break. In art. 101 the consolidation prints the start of the second paragraph ("La loi détermine les principes fondamentaux :") on the last line of the first list; it is split into its own paragraph (layout only, the words are unchanged). List dashes set in a smaller size at the body indent are kept.
- Unit layout: one file per article (art-NNN; art-NNN-N for the dotted articles such as 13.1 and 160.1), the preamble, and one structure file naming the article each title and chapter heading precedes.
- Typesetting is normalised once: NBSP to space, curly apostrophes to straight ones, curly double quotes to « », em dashes to en dashes, runs of spaces collapsed.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py and parse.py, chose the sources and wrote the decisions. No model wrote, summarised or transformed legal text: parse.py is deterministic code over the cached PDF.

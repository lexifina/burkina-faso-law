# Burkina Faso: law history in git

The law of Burkina Faso as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigueur_au.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `bf/`.

> **Not today's text.** The Constitution here stops at the revision of 5 November 2015. Three later constitutional laws are not applied, because no open source gives their text or their date (see below). This build is a preview: it is not on `main`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution du Burkina Faso | 1 | The Assemblée nationale's consolidation after Loi constitutionnelle n°072-2015/CNT du 05 novembre 2015, promulgated by Décret n°2015-1396/PRES-TRANS du 26 novembre 2015: the preamble, 177 articles (including the dotted articles 13.1, 96.1 and 160.1 to 160.6) and the structure of titles and chapters |

**Why the Constitution has one version.** The Constitution was adopted by referendum on 2 June 1991 and revised by eight laws between 1997 and 2015. The official LegiBurkina portal publishes it only as this one consolidation; the revision laws themselves are scans there (Loi 072-2015/CNT, for example), and scans are not transcribed. So the Constitution enters the history once, on 26 November 2015, credited to the publisher as the oldest version available. Its commit names the 1991 Constitution and the eight revision laws the consolidation lists on its cover. The consolidation's footnotes, which say how each revision changed each provision, are left out of the text.

**What is missing after 2015**

| Law | What we have | Why it is not applied |
| --- | --- | --- |
| Loi constitutionnelle n°045-2023/ALT (adopted 30 December 2023) | Text with a text layer, on the Assemblée législative de transition's site | No source gives its promulgation date (the Assemblée's list shows the placeholder 01/01/1900), so its version cannot be dated |
| Loi constitutionnelle n°033-2024/ALT (promulgated 21 November 2024, per the Assemblée's list) | A scan | No text layer, and scans are not transcribed |
| Loi n°004-2026/ALT du 20 janvier 2026 (révision de la constitution) | A one-page scan on LegiBurkina | No text layer |

The Code pénal (Loi n°025-2018/AN) and the data protection law were also examined. The Code pénal's 2019 amendment (Loi n°044-2019/AN) is not online, and a new Code pénal was adopted in October 2026. The data protection law of 2021 (Loi n°001-2021/AN) was repealed by Loi n°037-2026/ALP du 03 août 2026, which is published only as a scan with an OCR layer. Neither is built.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 37 say on 1 January 2020? | `python tools/en_vigueur_au.py 2020-01-01 constitution 37` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" HEAD -- constitution/art-037.md):constitution/art-037.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" HEAD -- constitution/art-037.md; git show "$($r):constitution/art-037.md"` |
| Which law wrote each paragraph of art. 37? | `git blame constitution/art-037.md` |
| Every change to an article, word by word | `git log -p --word-diff constitution/art-037.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short` |
| The whole Constitution on a date | `python tools/en_vigueur_au.py 2020-01-01 constitution` |
| Where an article sits (title, chapter) | `constitution/structure.md` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Ouagadougou (UTC), on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read.
- **The one version is dated by its promulgation decree,** Décret n°2015-1396/PRES-TRANS du 26 novembre 2015, as printed on the consolidation's cover. The date of its publication in the Journal officiel was not found.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- The repository is rebuilt from the same data a second time and must give identical hashes.
- The text is read from the PDF's own text layer (the file was made with Word, not scanned). The words are as printed; only line breaks, footnotes and typesetting are changed (see "How it is built").

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina. Where a version is not the act as enacted, as with the Constitution here, the first commit is credited to the publisher (the Secrétariat général du Gouvernement et du Conseil des ministres, which runs LegiBurkina) as the oldest version available. Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **The Constitution before 2015**, and the words each revision replaced (see above).
- **The Constitution after 2015**: Lois constitutionnelles 045-2023/ALT, 033-2024/ALT and 004-2026/ALT (see the table above).
- **Headings** (titres, chapitres) are not in the article files; they are gathered in `structure.md`, each line naming the article it precedes.
- **The consolidation's footnotes** and its cover page (the lists of revision laws and promulgation decrees).
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

`tools/fetch.py` downloads each file once with curl, at no more than three requests per second per host, cached by the sha256 of its URL. `tools/parse.py` reads only the cache: it reads the PDF's text layer with PyMuPDF, drops footnotes (9.8 pt) and footnote markers (superscripts), rebuilds paragraphs from the justified layout, splits the text into one file per article and writes `corpus.json`; the shared builder `tools/build.py` turns it into the commits. `REPRODUCE.md` lists every source, command, tool version and decision, and the result of the hash-for-hash rebuild.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [LegiBurkina](https://www.legiburkina.gov.bf/textesFondamentaux) (SGG-CM) | The official portal of Burkina Faso law, relaunched in 2026: fundamental texts, laws and decrees as PDFs | The Constitution's text and dates |
| [Assemblée nationale / Assemblée législative de transition](https://www.assembleenationale.bf/loip) | The répertoire of adopted laws (2018-2026), with PDFs of most of them | Probed: Loi constitutionnelle 045-2023/ALT (text) and 033-2024/ALT (scan) |
| [JOBF](https://jobf.gov.bf) | The Journal officiel, by paid subscription | Not used |
| The former LegiBurkina (legiburkina.bf) and sggcm.gov.bf, in the Internet Archive | Older consolidations (2002, 2012) and Journal officiel pages | Probed; not used yet |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Text: the Constitution du Burkina Faso as consolidated by the Assemblée nationale and published on LegiBurkina (Secrétariat général du Gouvernement et du Conseil des ministres); an official text of Burkina Faso, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En français

Ce dépôt retrace l'histoire du droit burkinabè dans git : un fichier par article, un commit par loi à la date de son entrée en vigueur, et la loi qui a modifié le texte comme auteur du commit. Il contient pour l'instant la Constitution du Burkina Faso dans la version consolidée par l'Assemblée nationale après la loi constitutionnelle n°072-2015/CNT du 05 novembre 2015 (décret de promulgation n°2015-1396/PRES-TRANS du 26 novembre 2015), publiée sur LegiBurkina. **Ce n'est pas le texte en vigueur aujourd'hui** : les lois constitutionnelles n°045-2023/ALT (date de promulgation introuvable), n°033-2024/ALT et n°004-2026/ALT (publiées seulement en images numérisées) ne sont pas appliquées. `python tools/en_vigueur_au.py 2020-01-01 constitution 37` affiche l'article 37 en vigueur à cette date, et `git blame constitution/art-037.md` indique la loi de chaque paragraphe. Ce dépôt ne constitue pas un conseil juridique.

# Burkina Faso: law history in git


The law of Burkina Faso as a git history: one file per provision, each version committed on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Burkina Faso's national law, which global-law reads at `burkina-faso/national/acts/`.

**What is in it now:** the Constitution of 2 June 1991, in one version: the Assemblée nationale's consolidation after Loi constitutionnelle n°072-2015/CNT of 5 November 2015, in force from 26 November 2015, with the preamble and 177 articles (including 13.1, 96.1 and 160.1 to 160.6). No statute yet. [`constitution/README.md`](constitution/README.md) lists every provision.

**Not today's text.** Three later constitutional laws are not applied (see [What it does not show](#what-it-does-not-show)), so for any day after 26 November 2015 this record gives the 2015 text, not the Constitution as revised since.

Each provision is one file in `constitution/` (`art-037.md` is Article 37, the President's term of office; `art-160-1.md` is Article 160.1); the preamble is `preambule.md`, and [`constitution/structure.md`](constitution/structure.md) names the article each title and chapter heading precedes.

The text is in French, as LegiBurkina publishes it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 37 of the Constitution (the President's term) | `git log -p --word-diff -- constitution/art-037.md` |
| Which law wrote each line of Article 37? | `git blame constitution/art-037.md` |
| Every version of Article 37, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution/art-037.md` |
| Article 37 as in force on 1 January 2020 | `python tools/en_vigueur_au.py 2020-01-01 constitution 37` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about the law of Burkina Faso](https://global-law.lexifina.com/v1/try_claude?country=burkina-faso)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=burkina-faso)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=droit+de+gr%C3%A8ve&jurisdictions=burkina-faso)**: a search of the law of Burkina Faso for "droit de grève" (the right to strike), returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in French or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add burkina-faso/national/acts
python3 tools/law.py show 2026-01-01 burkina-faso/national/acts/constitution/art-037.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Ouagadougou (UTC), on the day the version took effect, and carries it in its `In-force:` trailer:

- the one version is dated 26 November 2015, the day of Décret n°2015-1396/PRES-TRANS, which promulgated Loi constitutionnelle n°072-2015/CNT, as the consolidation's cover prints it; the day of its publication in the Journal officiel was not found.

The consolidation is not the Constitution as adopted, so its commit is credited to the publisher, the Secrétariat général du Gouvernement et du Conseil des ministres (which runs LegiBurkina), as the oldest version available, and names the 1991 Constitution and the eight revision laws the cover lists. The committer is always Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and both must match the corpus the history was built from; it also checks that every commit's trailers parse, that there are no merge commits and that no commit is dated in the future.
- `tools/build.py` writes the history from that corpus in one pass; a second build into an empty folder gave identical hashes. The results are in [`REPRODUCE.md`](REPRODUCE.md), and [`data/corpus.sha256`](data/corpus.sha256) gives the corpus's hash.
- The text is the PDF's own text layer (the file was made with Word, not scanned). Only line breaks, footnotes, the cover page and typesetting were changed, as [`LICENSE`](LICENSE) lists; the wording was not.

## What it does not show

- **The Constitution in force today.** Loi constitutionnelle n°045-2023/ALT (adopted 30 December 2023) has a text but no known promulgation date; n°033-2024/ALT (promulgated 21 November 2024, according to the Assemblée's list) and Loi n°004-2026/ALT of 20 January 2026 are published only as scans, and scans are not transcribed.
- **The Constitution before 2015**, and the words each of the eight revisions since 1991 replaced: LegiBurkina publishes only the 2015 consolidation as text, and its footnotes, which say how each revision changed each provision, are left out.
- **Headings** (titres, chapitres) are not in the article files; `structure.md` gathers them.
- **Any statute.** The Code pénal (Loi n°025-2018/AN) and the data protection law (Loi n°001-2021/AN) were examined, but their later changes are not online as text.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [LegiBurkina](https://www.legiburkina.gov.bf/textesFondamentaux) (Secrétariat général du Gouvernement et du Conseil des ministres) | Official portal of Burkina Faso law: fundamental texts, laws and decrees as PDFs | no, the 2015 consolidation only | The Constitution's text, and its date from the consolidation's cover |
| [Assemblée nationale / Assemblée législative de transition](https://www.assembleenationale.bf/loip) | List of adopted laws (2018-2026), with PDFs of most | as adopted | Consulted for the later constitutional laws; none applied |

## Licence

See [`LICENSE`](LICENSE). The text is the Constitution as consolidated by the Assemblée nationale and published on LegiBurkina, an official text of Burkina Faso reproduced with that attribution; the portal states no licence for legal texts. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## En français

L'histoire du droit burkinabè dans git : un fichier par article, chaque version enregistrée au jour de son entrée en vigueur, avec pour auteur la loi qui a modifié le texte. Le dépôt contient la Constitution du 2 juin 1991 dans la version consolidée par l'Assemblée nationale après la loi constitutionnelle n°072-2015/CNT (en vigueur depuis le 26 novembre 2015), publiée sur LegiBurkina. **Ce n'est pas le texte en vigueur aujourd'hui** : les lois constitutionnelles n°045-2023/ALT, n°033-2024/ALT et n°004-2026/ALT ne sont pas appliquées. Texte en vigueur à une date : `python tools/en_vigueur_au.py 2020-01-01 constitution 37`.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published

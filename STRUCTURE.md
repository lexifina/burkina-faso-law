# Structure du dépôt / Repository layout

Un dossier par texte, un fichier par article. Les noms sont en français, comme les textes.
One folder per act, one file per article. Names are in French, as the texts are.

| Dossier | Contenu |
| --- | --- |
| `constitution/` | Constitution du 2 juin 1991 : `preambule.md`, `art-001.md` … `art-169.md` (`art-013-1.md` = article 13.1), `structure.md` (titres et chapitres). Versions : consolidation de 2015, puis consolidation après les lois constitutionnelles n°045-2023/ALT et n°033-2024/ALT (en vigueur le 21 novembre 2024). |
| `chartes/<année>-<objet>/` | Chartes de la Transition publiées avec une couche texte. |
| `codes/<code>/` | Les codes (`codes/code-penal/`, `codes/code-du-travail/`, …) ; une version plus récente remplace les fichiers de la précédente dans le même dossier. Numérotation hiérarchique : `art-111-001.md` = article 111-1. |
| `lois/<année>/<numéro>-<objet>/` | Lois, lois organiques et constitutionnelles (hors codes). |
| `ordonnances/<année>/…`, `decrets/<année>/…`, `arretes/<année>/…` | Ordonnances, décrets, arrêtés. |
| `zatu/`, `kiti/`, `raabo/` `<année>/…` | Textes de la période révolutionnaire (1983–1991) : zatu (ordonnances), kiti (décrets), raabo (arrêtés). |
| `decisions/`, `circulaires/` `<année>/…` | Décisions et circulaires réglementaires publiées sur LegiBurkina. |
| `ohada/actes-uniformes/<objet>/` | Actes uniformes de l'OHADA, directement applicables au Burkina Faso (État partie), tels que publiés au Journal officiel de l'OHADA avec une couche texte native. |

Dans chaque dossier de texte : `README.md` (intitulé, source, date retenue et sa justification, couche texte),
`visas.md` (visas et préambule), `art-NNN.md` (un article par fichier ; `art-NNN-bis.md`, …), `signatures.md`
(formule finale et signataires). Un texte sans article repérable est en un seul fichier `texte-integral.md`.
Aucun dossier ne dépasse 1 000 entrées (sous-dossiers par année).

Each act folder holds `README.md` (title, source, chosen in-force date and why, text layer), `visas.md`,
one `art-NNN.md` per article and `signatures.md`. `corpus.json` lists every act (`bf/national/acts`).

## Commits

Un commit par version, daté à midi (Africa/Ouagadougou, UTC+0) du jour d'entrée en vigueur retenu, avec les trailers
`In-force` et `In-force-basis` (promulgation selon le répertoire de l'Assemblée législative lorsqu'il la donne ;
sinon décret de promulgation imprimé avec la loi ; sinon date du texte). Les dates antérieures à 1970 sont
horodatées 1970-01-01, la vraie date figurant dans le sujet et dans `In-force`. Copies secondaires :
`Source-status: secondary copy (...)` ; couche texte d'éditeur sur un scan : `Text-source: publisher OCR`.

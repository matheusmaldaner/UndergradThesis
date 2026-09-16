# Shared-material review (2026-09-16)

This review separates storage location from authorship. The files below were recovered from Stephen Wormald's Blue project directory, but that fact alone does not establish who authored each notebook or generated each output.

After HiPerGator access was restored, `stat` confirmed that all 30 files are owned by `stephen.wormald`, group `woodard`, with mode `0644`. A same-name SHA-256 search across `/orange/woodard/mkunzlermaldaner`, `/blue/woodard/mkunzlermaldaner`, and `/blue/uf-dsi/mkunzlermaldaner` found only the two exact Orange duplicates listed below. The search examined 20 same-name candidates; no author-controlled copies of the other 28 files were found.

## Inventory

`artifacts/raw/blue_explogic/` contains 30 files:

- 17 Jupyter notebooks;
- eight MiniNet prediction CSVs; and
- five Fashion-MNIST timing CSVs.

The CSVs contain machine-generated numeric outputs and no authorship or license metadata. The notebooks include both substantial overlap with notebooks in Matheus Kunzler Maldaner's Orange directories and distinct material.

## Comparison with author-controlled copies

Two Blue notebooks are byte-identical to Orange copies already in the archive:

| Blue copy | Author-controlled copy |
| --- | --- |
| `notebooks/config/csv_to_yaml_mnist.ipynb` | `orange_exp/notebooks/config/csv_to_yaml_mnist.ipynb` |
| `notebooks/DIFFLOGIC/config/csv_to_yaml_mnist.ipynb` | `orange_diff/notebooks/config/csv_to_yaml_mnist.ipynb` |

An exact normalized-code-cell comparison also found the following strongest overlaps. Percentages mean “matching nontrivial code cells divided by code cells in the Blue notebook”; they are evidence of shared lineage, not proof of authorship.

| Blue notebook | Strongest Orange comparison | Matching code cells |
| --- | --- | ---: |
| `Main.ipynb` | `orange_exp/notebooks/Main.ipynb` | 46/64 (72%) |
| `Timing.ipynb` | `orange_exp/notebooks/Main.ipynb` | 46/68 (68%) |
| `DIFFLOGIC/Main.ipynb` | `orange_eco/notebooks/Main.ipynb` | 19/22 (86%) |
| `DIFFLOGIC/Analysis.ipynb` | `orange_exp/notebooks/Analysis.ipynb` | 12/12 (100%) |
| `DIFFLOGIC/DecisionBoundary_wormald.ipynb` | `orange_exp/notebooks/DecisionBoundary_wormald.ipynb` | 20/20 (100%) |
| `DIFFLOGIC/DiffLogicSwitchingProbability_wormald.ipynb` | corresponding Orange ExpLogic notebook | 73/74 (99%) |
| `DIFFLOGIC/MiniNets_wormald.ipynb` | `orange_diff/notebooks/MiniNets.ipynb` | 27/48 (56%) |
| `DIFFLOGIC/DiffLogicSwitchingProbability_wormald-ciphar.ipynb` | Orange switching-probability notebook | 40/72 (56%) |

Other Blue notebooks had between 0% and 40% exact code-cell overlap with their nearest Orange comparison. Some filenames contain `_wormald`, and `Main.ipynb` and `Timing.ipynb` include a section titled “Creating MiniNets with Stephen Code.” Those facts make a blanket inference of sole authorship inappropriate.

## Comparison with the published ExpLogic archive

The complete public Git history of `matheusmaldaner/ExpLogic` was compared by SHA-256 against all 30 Blue files. Only the two configuration notebooks listed above appeared byte-for-byte in that history. All commits in that public repository are attributed to Matheus accounts, and the ExpLogic Zenodo record identifies Matheus as its sole creator and applies CC BY 4.0 to that deposit. Those facts clarify the published ExpLogic release but do not license the 28 files absent from it.

## Publication decision

All 30 files were moved to the separate private repository `matheusmaldaner/UndergradThesisRestrictedArchive`. The public repository excludes their bytes from its published Git history. It retains:

- provenance and checksum descriptions;
- aggregate Fashion-MNIST timing results; and
- confusion-count sufficient statistics that reproduce the Table 4-2 arithmetic without exposing per-example prediction records.

The restricted repository must remain private unless Stephen supplies publication permission and agreed attribution and licensing. The sanitized credential-bearing notebook is unrelated to this rights question. Its original bytes were never committed.

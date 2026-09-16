# Rights and attribution

This repository contains files with mixed provenance. License scopes are defined in [`LICENSE.md`](LICENSE.md).

## Author-controlled material

Files recovered from Matheus Kunzler Maldaner's Orange and personal thesis directories are preserved as research records. Existing licenses in the separately published implementation repositories continue to govern those repositories.

## Shared collaborator material

Thirty files were recovered from a shared project directory belonging to Stephen Wormald. HiPerGator reported `stephen.wormald` as owner, `woodard` as group, and mode `0644` for all 30. They are preserved in the separate private repository `matheusmaldaner/UndergradThesisRestrictedArchive`. Twenty-eight unique contents are absent from this public archive and its published Git history. Two configuration notebooks have byte-identical, author-controlled Orange copies that remain in the public archive; those equivalents are identified in `artifacts/RESTRICTED_ARTIFACTS.csv`.

The file-by-file comparison in [`docs/shared-material-review-2026-09-16.md`](docs/shared-material-review-2026-09-16.md) records filesystem ownership, exact duplicates, code-cell overlap with author-controlled Orange copies, and comparison with the public ExpLogic history. Filesystem ownership is evidence about the storage account, not a final copyright determination; separation avoids relying on an unsupported rights inference.

## Third-party software and datasets

This archive does not redistribute the MNIST or Fashion-MNIST datasets, Conda environments, Python packages, CUDA build products, or other reconstructable third-party dependencies. Model and prediction artifacts remain subject to any applicable upstream dataset and software terms.

Public confusion counts and aggregate timing results were derived during the private audit. They contain no per-example records or collaborator notebook code and are licensed with the other reconstruction outputs as described in [`LICENSE.md`](LICENSE.md).

## Credential sanitization

One visualizer notebook contained embedded OpenAI API-key strings. The original is excluded from Git, and the preserved copy is sanitized as documented in [`artifacts/SANITIZATION.md`](artifacts/SANITIZATION.md). A scan of the complete Git history confirms that no matching credential was ever committed. The historical key should still be revoked as account hygiene, but its status does not change the contents exposed by this repository.

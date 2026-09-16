# Public derived evidence

These small files were produced during the September 2026 private artifact audit. They preserve enough aggregate information to check the thesis's Table 4-2 classification arithmetic without publishing collaborator-owned per-example records.

- `mininet_confusion_counts.csv` records the threshold and `tp`, `tn`, `fp`, and `fn` counts for each of ten classes in four recovered model runs.
- `parent_classification_counts.csv` records the sample and correct-prediction counts for the parent model in the same four runs.

Run `python scripts/reproduce_mininet_table.py` to regenerate the public files under `results/`. The script verifies that all four runs and all 40 model/class pairs are present.

The source files' paths, sizes, and SHA-256 hashes are recorded in `artifacts/RESTRICTED_ARTIFACTS.csv`. Their bytes are stored only in the private `matheusmaldaner/UndergradThesisRestrictedArchive` repository because HiPerGator attributes all of them to `stephen.wormald` and redistribution permission has not been established.

# Undergraduate Thesis Reproducibility Archive

This repository is the central archival and reproducibility companion for Matheus Kunzler Maldaner's 2025 University of Florida undergraduate thesis on Differentiable Logic Gate Networks. It preserves the notebooks and experimental records that were previously distributed across HiPerGator storage, and it provides small, deterministic scripts for checking the thesis's quantitative results.

The current archival release is [`v0.1.0`](https://github.com/matheusmaldaner/UndergradThesis/releases/tag/v0.1.0).

The original implementation repositories remain separate because they have their own histories, releases, and Zenodo records. Exact repository versions are pinned in [`external-repositories.yml`](external-repositories.yml).

## Reconstruction disclosure

This repository was assembled in September 2026, approximately one year after the thesis was accepted and after the author graduated summa cum laude. The archival recovery, organization, documentation, and reproducibility audit were completed with assistance from OpenAI's **GPT-5.6 Sol** model using **medium reasoning effort**. That assistance occurred after the thesis had been accepted and the degree awarded; it was not involved in the original research, thesis writing, examination, or grading. Every reconstructed claim in this repository is tied to preserved artifacts and a reviewable script.

The archive intentionally distinguishes original files from later reconstruction:

- [`artifacts/raw/`](artifacts/raw/) contains byte-preserved, author-controlled historical files recovered from HiPerGator. One notebook with embedded credentials is stored as a documented sanitized copy.
- [`notebooks/cleaned/`](notebooks/cleaned/) and [`scripts/`](scripts/) were created in 2026 to make the preserved evidence easier to inspect.
- [`results/`](results/) contains deterministic outputs generated from the recovered files.
- [`ERRATA.md`](ERRATA.md) records confirmed corrections and unresolved claims.
- [`docs/accuracy-review-2026-09-16.md`](docs/accuracy-review-2026-09-16.md) gives the evidence-based accuracy assessment and publication recommendation.
- [`PROVENANCE.md`](PROVENANCE.md) maps thesis results to the available evidence.
- [`artifacts/NOTEBOOK_INDEX.csv`](artifacts/NOTEBOOK_INDEX.csv) provides a searchable inventory of the recovered notebooks.

## Reproduce the recovered MiniNet metrics

Only Python's standard library is needed:

```bash
python scripts/reproduce_mininet_table.py
python -m unittest discover -s tests -v
python scripts/verify_artifacts.py
python scripts/check_sensitive_strings.py
python scripts/build_notebook_index.py
```

The private artifact audit used recovered prediction CSVs to derive the confusion counts in [`artifacts/derived/mininet_confusion_counts.csv`](artifacts/derived/mininet_confusion_counts.csv). Those sufficient statistics reproduce the accuracy, precision, published recall-like value, and F1 entries in thesis Table 4-2 without redistributing collaborator-owned per-example files. The original notebook calculated recall as `tp / (tn + fn)`; the standard definition is `tp / (tp + fn)`. The reproduction script reports both values and writes the corrected results to [`results/mininet_table_reproduced.csv`](results/mininet_table_reproduced.csv).

## Archive status

| Area | Status |
| --- | --- |
| Historical notebooks | 43 public-archive notebooks recovered from author-controlled project trees; one credential-bearing notebook sanitized |
| MiniNet prediction CSVs | Audited privately; excluded from the public archive because all copies are owned by a collaborator account |
| Parent checkpoints | Five relevant MNIST checkpoints recovered |
| MiniNet size results | Partial provenance; exact table percentages remain unresolved |
| MiniNet timing results | Thesis-specific timing source remains unresolved |
| FPGA results | Implementation and synthesis artifacts exist; table sizes and some timings remain unreconciled |
| Visualizer | Structural graph functionality confirmed; some thesis descriptions exceed the released implementation |

The 30 Blue-directory copies are preserved in a separate private restricted archive. Twenty-eight unique contents are absent from this repository and its public history; two configuration notebooks remain only through byte-identical, author-controlled Orange copies. See [`RIGHTS_AND_ATTRIBUTION.md`](RIGHTS_AND_ATTRIBUTION.md) and the completed [`PUBLIC_RELEASE_CHECKLIST.md`](PUBLIC_RELEASE_CHECKLIST.md).

## Related repositories

- [OverleafUndergradThesis](https://github.com/matheusmaldaner/OverleafUndergradThesis) — thesis source
- [EcoLogic](https://github.com/matheusmaldaner/EcoLogic) — FPGA export and deployment ([Zenodo](https://doi.org/10.5281/zenodo.15099270))
- [ExpLogic](https://github.com/matheusmaldaner/ExpLogic) — MiniNet and explanation work ([Zenodo](https://doi.org/10.5281/zenodo.15099409))
- [DiffLogicVisualizer](https://github.com/matheusmaldaner/DiffLogicVisualizer) — graph inspection interface ([Zenodo](https://doi.org/10.5281/zenodo.15099266))
- [SaliencySlider](https://github.com/matheusmaldaner/SaliencySlider) — saliency interface discussed in the thesis ([Zenodo](https://doi.org/10.5281/zenodo.15093818))

## Repository policy

Raw archival files are never edited in place. Corrections belong in scripts, cleaned notebooks, derived results, or errata. Any future release should preserve the artifact manifest and checksums so readers can distinguish historical evidence from later documentation.

Licensing is applied by repository area as described in [`LICENSE.md`](LICENSE.md); historical artifacts are not relicensed by this reconstruction.

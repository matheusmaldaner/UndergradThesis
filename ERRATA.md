# Thesis errata and verification status

This document records findings from the 2026 artifact recovery. It does not alter the accepted 2025 thesis.

## Confirmed corrections

### Table 4-2 recall

The historical notebook uses `tp / (tn + fn)`. Standard recall is `tp / (tp + fn)`. During the private audit, recovered test predictions reproduced the published 10.7–11.2% column with the historical formula. Public confusion counts preserve the calculation without redistributing the per-example files. Correct class recalls are approximately 90.0–97.4%, with a four-run macro average of 94.26%.

### Number of recovered runs

The table's classification columns can be reproduced from four archived model runs (`model_000` through `model_003`). The prose says five models. No fifth prediction pair was found.

### Parent accuracy

The four recovered parent prediction sets have ten-class accuracies of 92.07%, 91.97%, 92.30%, and 92.12%, averaging 92.12%. A separate saved evaluation of `model_077` reports 92.15%. The exact 91.2% value in the thesis is not present in the recovered records and may be a transposition of 92.1%.

### Accuracy comparison

The parent percentage is ten-class accuracy. The MiniNet percentage is the macro average of ten one-versus-all accuracies. These quantities are not directly comparable, so the claim that 94.8% “surpassed” the parent should be removed or replaced with a comparison using the same tasks and decision rule.

### FPGA table arithmetic

For the row listing 724.28 microseconds on GPU and 280.52 microseconds on FPGA, the reduction is 61.27%, not 74%.

## Unresolved quantitative provenance

- The exact source records for the Table 4-2 size-reduction percentages have not been identified unambiguously.
- The exact source records for the Table 4-2 MNIST timing reductions have not been identified. Preserved 50,000-row timing files belong to a separate Fashion-MNIST experiment.
- FPGA model IDs, actual gate counts, plot points, table node counts, timing rows, and synthesis reports require a single reconciled dataset before making scaling claims beyond one million nodes.
- The saved Quartus report applies to the selected small model and does not verify the statement that the largest tested model occupied 13% of the FPGA.

## Software-description corrections

- General DiffLogic inference is not asymptotically `O(1)` as network size and depth grow.
- Combinational FPGA propagation has nonzero delay.
- The released visualizer exposes graph structure and learned gate-type distributions, but the inspected code does not implement the thesis's claimed input-dependent gate highlighting.
- The visualizer's released image endpoint requires corrected resizing and binary normalization before its uploaded-image predictions should be relied upon.

The detailed audit is preserved at [`docs/accuracy-review-2026-09-16.md`](docs/accuracy-review-2026-09-16.md).

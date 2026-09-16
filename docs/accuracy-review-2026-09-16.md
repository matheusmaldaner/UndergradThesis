# Thesis accuracy review (2026-09-16)

## Overall assessment

The recovered code, checkpoints, notebooks, synthesis products, released repositories, and experiment outputs support that the thesis's main engineering work was performed: Differentiable Logic Gate Networks were trained and inspected, class-specific reduced networks were constructed, models were exported toward FPGA deployment, and a graph visualizer was implemented. The audit found no evidence that the project as a whole was impossible or that its central implementations were invented after the fact.

Several quantitative and descriptive claims need narrower wording. The strongest problems are a nonstandard recall formula labeled as recall, a comparison between unlike accuracy definitions, one FPGA-table arithmetic error, and software behavior described beyond what appears in the released visualizer. Some timing, size-reduction, and FPGA-scaling claims remain unsupported by a single reconciled source record.

## Findings supported by recovered evidence

### MiniNet classification

Four recovered runs (`model_000` through `model_003`) support the classification columns in thesis Table 4-2. The private artifact audit converted the per-example files into public sufficient statistics in `artifacts/derived/`.

- Mean parent ten-class accuracy: **92.1160%**.
- Mean MiniNet one-versus-all accuracy: **94.6847%**.
- Mean MiniNet precision: **68.0930%**.
- Mean standard recall: **94.2573%**.
- Mean value from the thesis notebook's recall formula: **10.9821%**.
- Mean F1: **0.7868**.

These results make the reported classification table recognizable and reproducible at the arithmetic level. They also expose two interpretation errors:

1. The historical notebook computes the column called recall as `tp / (tn + fn)`. Standard recall is `tp / (tp + fn)`.
2. Parent accuracy is ten-class accuracy, while MiniNet accuracy is the macro average of ten one-versus-all accuracies. The 94.8% and 91.2% figures therefore do not establish that MiniNets surpassed the parent model.

The prose describes five trained models, but only four prediction pairs were recovered. The recovered parent runs average 92.12%, and a separate saved checkpoint evaluation reports 92.15%; no recovered record yields exactly 91.2%.

### MiniNet compression and timing

The notebooks support that graph tracing and pruning produced smaller class-specific structures. They do not provide a clean, authoritative reconstruction of every size-reduction percentage in Table 4-2. The preserved 50,000-row timing experiment uses Fashion-MNIST and therefore cannot verify the table's MNIST timing claims. Claims of an average 86% size reduction and 10% timing reduction should be presented as historical reported results unless a reconciled source table is recovered.

### FPGA implementation

The EcoLogic release, HDL-generation code, Quartus project material, reports, and bitstream support that FPGA export and compilation work occurred. One table entry is arithmetically wrong: reducing 724.28 microseconds to 280.52 microseconds is a **61.27%** reduction, not 74%.

The recovered synthesis report applies to a selected smaller design. It does not establish that the largest tested network used only 13% of the FPGA. The node counts, gate counts, plotted points, timing rows, and synthesis configurations need a single reconciled dataset before the reported scaling trend or largest-model utilization can be treated as independently verified.

### Complexity statement

The thesis describes general DiffLogic inference as `O(1)` compared with `O(L × N)` for a feed-forward network. A fixed compiled circuit can have constant latency relative to repeated inputs under a fixed hardware configuration, but inference does not remain asymptotically constant as network depth and size grow. Combinational FPGA inference also has nonzero propagation delay. The claim should be limited to fixed-architecture parallel hardware execution.

### DiffLogicVisualizer

The released frontend and backend support loading a model, inspecting graph structure, and viewing learned gate-type distributions. The audit did not find the claimed input-dependent highlighting of activated gates in the released implementation. The uploaded-image endpoint also needs corrected resizing and binary normalization before its predictions should be relied on. Descriptions of those behaviors should be framed as intended or future functionality unless another implementation is recovered.

## Evidence limitations

- The 30 collaborator-owned files used during part of the private audit are excluded from the public repository. Public confusion counts preserve the Table 4-2 metric calculation without redistributing those files.
- Historical notebooks record exploratory work and environment-specific paths; many are evidence of execution, not turnkey reproductions.
- The archive does not redistribute MNIST or Fashion-MNIST, Conda environments, package installations, or other reconstructable third-party material.
- Absence from the recovered archive does not prove that an experiment never occurred; it means the claim is not independently verified by the records found in the scoped storage search.

## Publication recommendation

The thesis can be made public with the accepted document left intact and this audit linked as a retrospective companion. The central work is credible. `ERRATA.md` should accompany the archive so readers can distinguish confirmed results, corrected calculations, and unresolved provenance.

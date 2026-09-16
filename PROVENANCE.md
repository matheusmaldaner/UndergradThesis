# Result provenance

| Thesis result | Preserved evidence | Reproduction | Status |
| --- | --- | --- | --- |
| Table 4-2 accuracy, precision, recall-like value, F1 | Public confusion-count sufficient statistics derived from four privately audited test-prediction CSVs | `python scripts/reproduce_mininet_table.py` | Arithmetic reproduced; recall formula corrected |
| Parent classification accuracy | Public sample/correct counts derived from the same private audit; saved `model_077` evaluation | Same script | Recovered runs average 92.12%; thesis says 91.2% |
| Threshold selection | Threshold metadata extracted during the private audit | `artifacts/metadata/mininet_thresholds.json` | Raw training predictions remain restricted |
| MiniNet gate reduction | Historical construction notebooks and printed reduced structures | No authoritative clean reproduction yet | Reduction occurred; exact Table 4-2 percentages unresolved |
| MiniNet inference timing | Aggregate summary from a privately audited, separate Fashion-MNIST timing experiment | `results/fashion_mnist_timing_summary.json` | Raw timing rows restricted; experiment cannot verify thesis percentages |
| FPGA functionality | EcoLogic v1.0.0, generated HDL, Quartus bitstream and reports | External repository pinned by commit | Implementation and successful compilation supported |
| FPGA timing/scaling | `FPGA_Computation_Time.xlsx`, plots, thesis table, one saved Quartus project | Manual reconciliation documented in audit | Inconsistent; not fully verified |
| DiffLogicVisualizer graph inspection | DiffLogicVisualizer v1.0.0 backend/frontend and notebook | External repository pinned by commit | Structural inspection supported |
| Input-dependent visualizer highlighting | Released visualizer code | Static inspection and build checks in audit | Not found in released implementation |

## Storage origins

- `orange_exp`: `/orange/woodard/mkunzlermaldaner/_MAINBACKUP/EXPLOGIC`
- `orange_diff`: `/orange/woodard/mkunzlermaldaner/_MAINBACKUP/DIFFLOGIC`
- `orange_eco`: `/orange/woodard/mkunzlermaldaner/_MAINBACKUP/ECOLOGIC`
- `orange_thesis`: `/orange/woodard/mkunzlermaldaner/THESIS`
- `orange_visualizer`: `/orange/woodard/mkunzlermaldaner/VISUALIZER/DiffLogicVisualizer`
- `orange_fpga_backup2`: `/orange/woodard/mkunzlermaldaner/_BACKUP2/FPGA`
- `orange_fpga_past`: `/orange/woodard/mkunzlermaldaner/_PASTPROJECTS/FPGA`
- `orange_skeptic`: `/orange/woodard/mkunzlermaldaner/SKEPTIC/schoolhouse_ex/X_StateEmbedding`
The private audit also examined `/blue/woodard/stephen.wormald/project/DiffLogic/0_eXpLogic`. HiPerGator attributes all 30 recovered files there to `stephen.wormald`; those files were moved to a separate private restricted archive and are not distributed here. See [`RIGHTS_AND_ATTRIBUTION.md`](RIGHTS_AND_ATTRIBUTION.md).

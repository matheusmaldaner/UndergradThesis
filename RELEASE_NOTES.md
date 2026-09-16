# Release notes

## Planned v0.1.0 — reconstructed preservation archive

This release collects the thesis-era notebooks and supporting evidence recovered from HiPerGator in September 2026. It is a retrospective reproducibility archive and was not part of the thesis submitted or examined in 2025.

### Included

- Historical notebooks from the author-controlled thesis, DiffLogic, ExpLogic, EcoLogic, visualizer, FPGA, and SKEPTIC project trees.
- Public sufficient statistics derived from four privately audited MiniNet runs, plus five author-controlled MNIST checkpoints.
- A deterministic reconstruction of the recoverable Table 4-2 classification metrics.
- Corrected recall values and explicit preservation of the historical erroneous formula.
- A separately labeled aggregate summary of the privately audited Fashion-MNIST timing experiment.
- SHA-256 manifests, notebook inventory, provenance mapping, errata, and automated verification.
- A documented sanitized copy of one notebook that contained embedded credentials.

### Confirmed before release

- Raw local artifacts match their recorded HiPerGator sources.
- The reconstructed outputs are stable in local tests and GitHub Actions.
- No credential patterns remain in proposed Git content.
- All 30 files owned by the collaborator account on HiPerGator are excluded from the public repository history and preserved in a separate private restricted archive.

The historical credential was never committed; its revocation remains a separate account-security follow-up.

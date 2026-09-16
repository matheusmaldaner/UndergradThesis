# Public-release checklist

This checklist records the preparation of the public preservation archive.

- [x] Recover thesis-related notebooks from the identified HiPerGator project trees.
- [x] Recover the consolidated MiniNet prediction files and relevant checkpoints.
- [x] Record origins, SHA-256 checksums, and publication status for raw artifacts.
- [x] Verify every raw local artifact against its original HiPerGator path.
- [x] Add a deterministic Table 4-2 reconstruction and tests.
- [x] Add provenance, errata, attribution, and AI-assistance disclosure.
- [x] Scan the proposed repository content for credentials.
- [x] Sanitize the credential-bearing visualizer notebook and document the transformation.
- [x] Compare all recovered Blue files with author-controlled Orange copies and the complete public ExpLogic Git history.
- [x] Verify that the unsanitized credential-bearing notebook and its key never entered Git history.
- [x] Remove all 30 `stephen.wormald`-owned files from the public archive and preserve them in a separate private restricted repository.
- [x] Define licenses and rights scopes for reconstruction code, documentation, derived results, and historical artifacts in `LICENSE.md`.
- [x] Change `matheusmaldaner/UndergradThesis` from private to public.
- [x] Create a versioned GitHub release after the public commit passes CI.
- [x] Add the public archive link to the thesis and implementation repositories.

Do not treat the checked reconstruction items as retrospective participation in the original thesis. The repository-level disclosure in the README must remain in public releases.

Account-security note: revoke or independently confirm revocation of the historical OpenAI API key remaining in the original HiPerGator file. The key never entered this repository, so this is separate from publication readiness.

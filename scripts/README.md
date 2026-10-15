# Scripts

Scripts in this directory are for bounded, local, reproducible evidence collection. They must not target public or third-party systems. Any script that changes state must document a cleanup path and record its exit code in the run manifest.

## Evidence utilities

- `index_evidence.py`: Scans all experiment logs and outputs, computes SHA-256 digests, and generates `evidence/checksums.sha256` and `evidence/index.csv`. Supports `--verify` to validate artifact checksums.

# Cybersecurity Practicals Evidence Repository

This repository records authorized, local cybersecurity practicals with reproducible commands, raw output, genuine screenshots when available, cleanup verification, and honest result statuses. It is intended for professor review: a reviewer can inspect the report, follow its linked log, verify the target scope, and recompute artifact hashes.

## Scope and safety

Work is limited to loopback or deliberately vulnerable local lab applications. Public hosts, shared networks, real recipients, real credentials, and unrelated traffic are out of scope. See [`docs/safety-and-scope.md`](docs/safety-and-scope.md) and [`docs/lab-architecture.md`](docs/lab-architecture.md).

Experiment 1 is skipped at the user's request. Experiment 4 is blocked because its official source manual was not supplied. Experiment 5's second filename was identified as a duplicate in the supplied inventory, but only `CS_Exp5.docx` was accessible locally; no duplicate work was performed.

## Status dashboard

| Experiment | Status | Report | Screenshots | Output/report artifact | Blocker or limitation |
|---|---|---|---:|---|---|
| 1 | NOT STARTED — user skipped | [report](experiments/exp01-virtual-lab/README.md) | 0 | — | Explicitly skipped |
| 2 | PARTIAL | [report](experiments/exp02-social-engineering/README.md) | 0 | [local QR](experiments/exp02-social-engineering/outputs/demo_qr.png) | SET/mail delivery unavailable; local QR verified |
| 3 | PARTIAL | [report](experiments/exp03-cryptanalysis/README.md) | 0 | [supplemental log](experiments/exp03-cryptanalysis/logs/20261012_035200_supplemental-demo.log) | CrypTool 2 unavailable; supplemental substitute only |
| 4 | BLOCKED | [missing-manual note](docs/EXPERIMENT-04-MISSING.md) | 0 | — | Official source manual missing |
| 5 | PARTIAL | [report](experiments/exp05-vulnerability-scanning/README.md) | 0 | [Nmap output](experiments/exp05-vulnerability-scanning/logs/20261012_040100_nmap-port80.log) | DVWA absent; bounded loopback port check only |
| 6 | PARTIAL | [report](experiments/exp06-password-audit/README.md) | 0 | [sample hash](experiments/exp06-password-audit/outputs/hash.txt) | Hashcat absent; John lacks raw-MD5 format |
| 7 | BLOCKED | [report](experiments/exp07-sqli/README.md) | 0 | [precondition log](experiments/exp07-sqli/logs/20261012_041500_dvwa-precondition.log) | Local DVWA unavailable |
| 8 | BLOCKED | [report](experiments/exp08-xss/README.md) | 0 | [precondition log](experiments/exp08-xss/logs/20261012_041500_dvwa-precondition.log) | Local DVWA unavailable |
| 9 | BLOCKED | [report](experiments/exp09-owasp-zap/README.md) | 0 | [precondition log](experiments/exp09-owasp-zap/logs/20261012_041500_precondition.log) | Local target and ZAP unavailable |
| 10 | PARTIAL | [report](experiments/exp10-packet-analysis/README.md) | 0 | [reviewed PCAP](experiments/exp10-packet-analysis/outputs/loopback_capture.pcap) | tcpdump permissions/GUI screenshot unavailable; dumpcap/TShark evidence retained |
| 11 | BLOCKED | [report](experiments/exp11-firewall-ids/README.md) | 0 | [baseline log](experiments/exp11-firewall-ids/logs/20261012_050100_baseline-curl.log) | No disposable sandbox; UFW/Snort/sudo unavailable |
| 12 | BLOCKED | [report](experiments/exp12-dos-mitigation/README.md) | 0 | [baseline log](experiments/exp12-dos-mitigation/logs/20261012_050500_apache-baseline.log) | hping3/Apache/UFW/Snort unavailable |
| 13 | PARTIAL | [report](experiments/exp13-assessment-compliance/README.md) | 0 | [assessment summary](experiments/exp13-assessment-compliance/outputs/assessment_summary.md) | Apache inactive; UFW/APT unavailable |

**Current count:** 0 PASS, 6 PARTIAL, 6 BLOCKED, 0 FAIL, and 1 user-skipped experiment.

The authoritative current dashboard is [`STATUS.md`](STATUS.md). The aggregate result is in [`reports/summary.md`](reports/summary.md).

## Repository layout

- `docs/` — source inventory, architecture, scope, and experiment summaries
- `experiments/` — per-experiment logs, outputs, evidence, and report
- `evidence/index.csv` — repository-wide evidence table
- `manifest/` — environment and run manifest
- `reports/` — findings and aggregate summary

## Reproducibility and evidence

Commands are recorded without secrets. Logs are raw command output where practical. Evidence filenames use timestamps and experiment/step identifiers. A professor can verify an artifact by checking its path in `evidence/index.csv` and recomputing the SHA-256 in `evidence/checksums.sha256`. A checksum verifies file integrity after capture; it is not independent proof of the experiment's truth.

## Git sharing

The repository is local until explicitly pushed. The requested remote is `https://github.com/chiragkoyande/cslab.git`; no credentials or tokens belong in this repository.

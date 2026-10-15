# Safety and scope

## Authorized scope

This repository is for practical work performed by the repository owner in a controlled local lab. The intended targets are `127.0.0.1`, `localhost`, loopback services, or deliberately vulnerable applications explicitly started for this practical. No public IP, college/company system, shared Wi-Fi device, or third-party website is an approved target.

## Operating constraints

- Experiment 1 is skipped at the user's request.
- Experiment 2 uses a local benign QR demonstration and synthetic/offline mail data only. No Gmail password, app password, real recipient, phishing delivery, or credential collection is allowed.
- Experiments 5, 7, 8, and 9 use local DVWA only when its URL is verified before the test.
- Experiment 6 uses only the intentionally weak sample password/hash and a small synthetic wordlist.
- Experiment 10 captures only intentionally generated loopback/internal traffic. Unreviewed PCAPs are excluded by `.gitignore`.
- Experiment 11 firewall changes are permitted only in an isolated disposable sandbox. The recovery command is recorded before any change, and temporary rules must be removed.
- Experiment 12 permits only the manual's bounded ten SYN packets to `127.0.0.1:80`, one packet per second. It is not a flood or stress test.
- No destructive commands, broad protection disabling, internet exposure, exploit modules, or real credentials are used.

## Evidence integrity

Raw logs are preserved. Original screenshots, when available, are not edited. Derived annotations must be clearly labeled. SHA-256 checksums in `evidence/checksums.sha256` record file integrity at manifest time; they do not prove the truth of an underlying experiment by themselves.

## Cleanup

Temporary servers, scans, stored XSS content, custom IDS rules, firewall rules, and promiscuous mode changes must be stopped or removed. Cleanup status is recorded in each experiment report and in `manifest/run-manifest.json`.

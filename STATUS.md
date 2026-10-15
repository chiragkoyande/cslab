# Experiment status

Last updated: 2026-10-15 18:50 +05:30 after evidence indexing, checksum review, findings compilation, and Git verification.

| State | Experiments |
|---|---|
| Completed | Execution review and cleanup for all accessible experiment scopes; repository evidence indexing, checksum review, findings cataloging, and Git verification |
| In progress | None |
| Blocked | 4 — official source manual not supplied; 7, 8, 9 — local DVWA/ZAP unavailable; 11 — no disposable firewall/IDS sandbox; 12 — hping3/Apache/UFW/Snort unavailable |
| Partial | 2, 3, 5, 6, 10, 13 |
| User skipped | 1 |

Statuses will be changed only after the relevant command/UI step, observed output, and cleanup have been recorded. A `PARTIAL` or `BLOCKED` result is never counted as a pass.

## Current preflight blockers

- No VirtualBox/VMware command was detected on the Fedora host.
- No screenshot utility using a live desktop was detected; Firefox is available for possible headless browser screenshots, but GUI evidence may remain unavailable.
- Host `/home` has approximately 3.6 GiB free, so large VM/container/package downloads require review.
- No Kali VM was found. DVWA, Snort, ZAP, Hashcat, Nikto, hping3, UFW, SET, and CrypTool 2 were not available on the host.
- Genuine GUI screenshots were unavailable; reports link raw logs and real non-screenshot artifacts instead.

## Cleanup review

- Experiment 2 local demo server: stopped; port 18082 failed post-cleanup curl.
- Experiment 10 HTTP/UDP/DNS test servers and dumpcap: stopped; ports 18083/18084/15353 closed; loopback remained without `PROMISC`.
- Experiment 11 baseline server: stopped; port 18080 closed.
- No firewall rule, stored XSS payload, package update, or remote scan was performed.

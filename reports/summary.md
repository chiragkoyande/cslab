# Practical results summary

This summary reflects the observed runs on Fedora 43 at `/home/chiragk/Projects/cslab`. It is based on linked logs/artifacts rather than the source manuals' sample conclusions.

| Status | Count |
|---|---:|
| PASS | 0 |
| PARTIAL | 6 |
| BLOCKED | 6 |
| FAIL | 0 |
| NOT STARTED / user skipped | 1 |

## Experiment results

| Experiment | Status | Evidence-grounded result |
|---|---|---|
| 1 | NOT STARTED — user skipped | No VM work performed by explicit user direction. |
| 2 | PARTIAL | Local harmless QR/page generated and curl-verified; SET, mail delivery, and screenshot unavailable. |
| 3 | PARTIAL | Python/OpenSSL supplemental Caesar/Playfair/hash/frequency output ran; CrypTool 2 and Enigma Analyzer unavailable. |
| 4 | BLOCKED | Official source manual not supplied; no procedure invented. |
| 5 | PARTIAL | Loopback port-80 checks ran; DVWA/Apache inactive, Nikto/Metasploit unavailable. |
| 6 | PARTIAL | Synthetic MD5 matched the source; Hashcat missing and John raw-MD5 unsupported. |
| 7 | BLOCKED | Local DVWA probe failed before any SQLi payload. |
| 8 | BLOCKED | Local DVWA probe failed before any XSS payload. |
| 9 | BLOCKED | Local DVWA and ZAP unavailable; no scan. |
| 10 | PARTIAL | Reviewed 20-frame loopback PCAP analyzed with TShark; direct tcpdump and GUI screenshots unavailable. |
| 11 | BLOCKED | Read-only baseline only; no host firewall/IDS state change. |
| 12 | BLOCKED | Exact bounded SYN test not run because required tools/service were absent. |
| 13 | PARTIAL | Nmap report ran against loopback port 80; Apache inactive, UFW/APT unavailable. |

No result is counted as PASS. The final repository contains no real credentials, mail credentials, stored XSS content, remote targets, or unrelated PCAP traffic. The final loopback PCAP was reviewed and narrowed to intentionally generated traffic before retention.

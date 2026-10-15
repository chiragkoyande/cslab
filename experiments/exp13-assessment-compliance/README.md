# Experiment 13 — Vulnerability assessment and compliance review

**Source:** `CSL_EXP13.pdf`  
**Status:** `PARTIAL`

## Aim and required tools

The manual studies vulnerability-assessment reports and security-compliance practices using Kali, Nmap, Apache2, UFW, APT, curl, and a terminal. It asks for Nmap/Apache checks, `curl -I http://localhost`, `nmap -sV -sC -p 80 127.0.0.1 -oN vulnerability_report.txt`, HTTP headers/title scripts, `ufw status verbose`, and `apt list --upgradable`.

## Scope and safety

Only local Apache/loopback is allowed. Package updates will not be applied automatically. Server-header disclosure and pending updates will be reported as observations unless independent evidence supports a stronger claim.

## Procedure and evidence

1. Confirmed Nmap 7.92 and Apache/httpd 2.4.68. The service manager reported httpd inactive.
2. Confirmed the approved target as `127.0.0.1:80`. `curl -I` failed with exit code 7 because port 80 was closed.
3. Ran the source-aligned `nmap -sV -sC -p 80 127.0.0.1 -oN vulnerability_report.txt`; the actual report records TCP 80 closed. The HTTP header/title scripts likewise had no service to inspect.
4. Checked UFW; the command is unavailable on Fedora. Checked the source's `apt list --upgradable`; `apt` is unavailable and returned exit code 127. No package update was attempted.
5. Wrote [`assessment_summary.md`](outputs/assessment_summary.md) with findings, impact, recommendations, and confidence/status labels. It does not call the closed port a vulnerability.

Logs: [`Nmap version`](logs/20261012_051000_nmap-version.log), [`Apache status`](logs/20261012_051000_apache-status.log), [`curl`](logs/20261012_051000_curl-localhost.log), [`Nmap report`](logs/20261012_051000_nmap-report.log), [`HTTP scripts`](logs/20261012_051000_http-scripts.log), [`UFW`](logs/20261012_051000_ufw-status.log), and [`APT`](logs/20261012_051000_apt-upgradable.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 05:10 +05:30 | No GUI screenshot was captured; command reports are linked. |

## Result and cleanup

Result: `PARTIAL`. Nmap and the loopback target check ran successfully, but Apache was inactive and port 80 was closed; UFW and APT are unavailable on this Fedora host. No temporary service or system state change was made, so no service cleanup was required.

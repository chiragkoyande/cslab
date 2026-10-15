# Experiment 9 — OWASP ZAP web-application vulnerability scanning

**Source:** `Experiment_9_OWASP_ZAP_Web_Application_Vulnerability_Scanning.docx`  
**Status:** `BLOCKED`

## Aim and required tools

The manual aims to explore OWASP ZAP scanning against an authorized DVWA or Juice Shop. It lists Kali, VMware Workstation, ZAP, a deliberately vulnerable web application, a browser, and connectivity between testing and target VMs. The procedure installs `zaproxy`, launches it, runs an authorized automated scan, reviews alerts, and saves a report.

## Preconditions and safety

The target URL must be verified as loopback/local before scanning. Only that target will be configured in ZAP. Alerts will be manually reviewed and labeled for confidence/false-positive risk.

## Procedure and evidence

Checked for `zaproxy`/`zap.sh`; neither was installed. A curl probe to the approved local candidate `http://127.0.0.1/dvwa/` failed with exit code 7 because no local web service was listening. No ZAP process was launched and no scan was attempted. The precondition log is [`precondition.log`](logs/20261012_041500_precondition.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 04:15 +05:30 | ZAP and the local target were unavailable; no scan screenshot is claimed. |

## Result and cleanup

Result: `BLOCKED` because both the required local target and ZAP executable were unavailable. No report was exported and no cleanup beyond the precondition check was required.

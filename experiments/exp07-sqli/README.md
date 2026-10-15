# Experiment 7 — SQL injection and blind SQL injection

**Source:** `CSL_EXP7_SQLI.pdf`  
**Status:** `BLOCKED`

## Aim and source requirements

The manual demonstrates SQL Injection and Blind SQL Injection in DVWA using a normal ID, the Boolean SQLi input `1' OR '1'='1' #`, and blind true/false inputs `1' AND '1'='1' #` and `1' AND '1'='2' #`.

## Scope and safety

Only a verified local DVWA instance at loopback is allowed. No payload will be sent to any other site or database. The DVWA security level and login state will be recorded without committing credentials.

## Procedure and evidence

Confirmed the required local DVWA precondition before any payload: curl probes to `http://127.0.0.1/dvwa/`, `http://127.0.0.1/DVWA/`, and `/dvwa/login.php` all failed with exit code 7 because no local HTTP service was listening. Consequently, the normal ID query and all three documented SQLi/blind-SQLi inputs were not sent. The precondition log is [`dvwa-precondition.log`](logs/20261012_041500_dvwa-precondition.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 04:15 +05:30 | DVWA was unavailable; no payload screenshot is claimed. |

## Result and cleanup

Result: `BLOCKED` because the required local DVWA target was not running. No database was modified, no payload was sent, and no external target was contacted. There is no cleanup beyond the failed precondition check.

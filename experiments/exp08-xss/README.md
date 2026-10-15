# Experiment 8 — Reflected and stored XSS

**Source:** `CSL_EXP8_XSS.pdf`  
**Status:** `BLOCKED`

## Aim and source requirements

The manual demonstrates harmless reflected and stored XSS in DVWA. It specifies the normal input `User` and the payload `<script>alert('XSS')</script>` at low security.

## Scope and safety

Only a verified local DVWA page may receive the payload. The payload is intentionally harmless and must be removed from the stored-XSS field after evidence capture. No cookies, tokens, credential forms, or external callbacks will be used.

## Procedure and evidence

Confirmed the required local DVWA precondition before any input: curl probes to `http://127.0.0.1/dvwa/`, `http://127.0.0.1/DVWA/`, and the reflected-XSS path all failed with exit code 7 because no local HTTP service was listening. The normal input and harmless alert payload were not sent. The precondition log is [`dvwa-precondition.log`](logs/20261012_041500_dvwa-precondition.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 04:15 +05:30 | DVWA was unavailable; no browser alert screenshot is claimed. |

## Result and cleanup

Result: `BLOCKED` because the required local DVWA target was not running. No XSS payload was stored, so no stored-content cleanup was necessary.

# Experiment 2 — Social engineering / SET

**Source:** `exp2 cyber.pdf`  
**Status:** `PARTIAL`

## Aim and source requirements

The manual aims to simulate social-engineering attacks using SET in a controlled Kali environment. It asks for Kali Linux and VirtualBox, then describes SET's legal disclaimer, Social-Engineering Attacks menu, QR Code Generator Attack Vector, and a Mass Mailer / Single Email workflow using a predefined template.

## Safety adaptation

The manual's Gmail sender and app-password steps cannot be executed. The safe scope permits only a benign QR target at `127.0.0.1` or an offline/local mail preview with synthetic data. No real recipient, credential, Gmail/app password, phishing delivery, or collection form will be used.

## Procedure attempted

1. Checked for `setoolkit`; no executable was found. `type set` showed only the zsh shell builtin, not SET.
2. Checked local QR libraries. Python's `qrcode` module was available, so a QR image was generated for `http://127.0.0.1:18082/demo.html`.
3. Served the clearly labeled page with Python's HTTP server bound to `127.0.0.1` only. `curl` returned the page and exit code 0.
4. Attempted a genuine Firefox headless screenshot. Firefox entered headless mode but did not produce the requested file on the first attempt and timed out on the absolute-path retry; no screenshot is claimed.
5. Stopped the temporary server. A post-cleanup curl failed with exit code 7, confirming that port 18082 was no longer serving the page.

Logs: [`tool-check`](logs/20261012_034200_tool-check.log), [`QR module check`](logs/20261012_034200_qr-module-check.log), [`QR generation`](logs/20261012_034300_qr-generation.log), [`curl`](logs/20261012_034400_demo-curl.log), [`browser attempt`](logs/20261012_034600_browser-screenshot.log), and [`cleanup`](logs/20261012_034700_cleanup.log). The generated QR is [`demo_qr.png`](outputs/demo_qr.png); its target URL is recorded in the QR-generation log.

## Evidence

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 03:47 +05:30 | GUI screenshot capture was unavailable; no fabricated screenshot is included. |

## Observations and result

Observed result: the local-only QR artifact and page were produced and verified with curl. SET itself was unavailable, the manual's email workflow was not attempted because it requires external credentials/delivery, and GUI screenshot capture failed. The evidence supports a safe local demonstration only; it does not support completion of the SET workflow. Result: `PARTIAL`.

## Cleanup

The temporary server was stopped; post-cleanup curl exit code 7 confirmed it was unavailable. No mail was sent and no credential was requested or stored.

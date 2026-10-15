# Experiment 11 — Firewall access control and Snort IDS

**Source:** `CSL_EXP11_Firewall.pdf`  
**Status:** `BLOCKED`

## Aim and source requirements

The manual implements firewall policies with UFW/iptables and observes Snort IDS alerts. It specifies a local Python server on `127.0.0.1:8080`, UFW status/allow/deny commands, an iptables loopback drop rule, a temporary Snort rule, curl tests, and removal/restoration commands.

## Safety and preconditions

The host is not assumed to be a disposable Kali VM. Baseline firewall/routing state and exact recovery commands must be recorded before any change. If an isolated sandbox is not available, only read-only checks are safe and the state-changing portion remains blocked.

## Procedure and evidence

1. Recorded the host identity, interfaces, and non-interactive sudo state. The current user is unprivileged for firewall inspection; `iptables -S` returned permission denied and sudo requires a password.
2. Checked the named tools. `iptables` exists, but UFW and Snort are absent. No firewall rule was added, deleted, enabled, or disabled.
3. Started a temporary Python HTTP server bound to `127.0.0.1:18080` as a harmless connectivity baseline. Curl succeeded with exit code 0, then the server was stopped and the port was confirmed closed.

Logs: [`precondition`](logs/20261012_050000_firewall-ids-precondition.log), [`interfaces`](logs/20261012_050000_interfaces.log), [`sudo check`](logs/20261012_050000_sudo-check.log), and [`baseline curl/cleanup`](logs/20261012_050100_baseline-curl.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 05:01 +05:30 | No firewall/IDS GUI screenshot was captured. |

## Result and cleanup

Result: `BLOCKED`. The core UFW/iptables state-change and Snort alert steps were not executed because this is an active Fedora host without a disposable sandbox, UFW/Snort are unavailable, and sudo is not non-interactive. No firewall or IDS state was changed; the temporary test server was cleaned up and port 18080 was closed.

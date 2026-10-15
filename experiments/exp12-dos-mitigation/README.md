# Experiment 12 — Controlled DoS-defense observation

**Source:** `CSL_EXP12_DoS.pdf`  
**Status:** `BLOCKED`

## Aim and source requirements

The manual evaluates firewall, IDS, and traffic monitoring around Apache using hping3. The permitted test is exactly `sudo hping3 -S -p 80 -c 10 -i u1000000 127.0.0.1`: ten SYN packets, one per second, to local port 80.

## Safety and preconditions

This is not a stress test. Apache availability, resource state, and monitoring must be checked before and after. No remote target, spoofing, flood mode, rate escalation, or count escalation is allowed. If health degrades, the test stops immediately.

## Procedure and evidence

1. Checked the required tools and services. `httpd` is installed but inactive; hping3, UFW, and Snort are absent. Tcpdump is installed but direct capture requires a capability not available to this user.
2. Verified the loopback interface and checked Apache availability with `curl --head http://127.0.0.1:80`; curl failed with exit code 7 because port 80 was closed.
3. Did not run the hping3 command because the target Apache service and monitoring/firewall preconditions were not satisfied. No SYN packets were generated.

Logs: [`tool precondition`](logs/20261012_050500_tool-precondition.log), [`Apache baseline`](logs/20261012_050500_apache-baseline.log), and [`interface check`](logs/20261012_050500_interface-check.log).

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 05:05 +05:30 | No DoS-test screenshot is claimed because the bounded test was not run. |

## Result and cleanup

Result: `BLOCKED`. The exact ten-packet loopback command was not executed because hping3, Apache service availability, UFW, and Snort preconditions were missing. No system health degradation or firewall/IDS state change occurred, and no real-world DoS claim is made.

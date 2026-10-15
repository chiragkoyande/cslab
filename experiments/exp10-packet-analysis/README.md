# Experiment 10 — Packet capture and protocol analysis

**Source:** `CSL_EXP10_PCAP.pdf`  
**Status:** `PARTIAL`

## Aim and source requirements

The manual aims to use tcpdump and Wireshark in promiscuous mode to analyze TCP, UDP, DNS, and ICMP. It asks for interface discovery, capture to `network_capture.pcap`, Wireshark filters `icmp`, `dns`, and `tcp`, and restoration of promiscuous mode.

## Safety adaptation

The manual's public examples such as `8.8.8.8` and `google.com` will not be used. Traffic will be intentionally generated on loopback or an isolated internal interface. The original promiscuous-mode state will be recorded before any change and restored afterward. PCAP content will be inspected for secrets before inclusion.

## Procedure and evidence

1. Verified tcpdump 4.99.6, TShark/Wireshark 4.6.1, and available capture interfaces. Loopback `lo` was selected; it had no `PROMISC` flag before or after the test.
2. A direct tcpdump capture attempt failed with “You don't have permission to perform this capture … CAP_NET_RAW may be required.” Non-interactive sudo was unavailable. The exact failure is [`tcpdump-capture.log`](logs/20261012_042100_tcpdump-capture.log) and the sudo check is [`sudo-check.log`](logs/20261012_042200_sudo-check.log).
3. Wireshark's capability-enabled `dumpcap` was used as a clearly labeled supplemental capture path. The traffic was generated only on loopback: HTTP to `127.0.0.1:18083`, one UDP datagram to `127.0.0.1:18084`, a controlled DNS-format request/response on `127.0.0.1:15353`, and two ICMP pings to `127.0.0.1`.
4. The first loopback capture was discarded after review showed unrelated local JSON traffic. A second capture was narrowed and then frame-filtered with `editcap`; the final reviewed [`loopback_capture.pcap`](outputs/loopback_capture.pcap) contains 20 frames, all 127.0.0.1 traffic: 13 TCP, 3 UDP (including 2 DNS), and 4 ICMP.
5. TShark filters equivalent to `icmp`, `dns` (with the high-port DNS decode), `tcp`, and `udp` were applied. Logs are under [`logs/`](logs/), including the final protocol hierarchy and per-protocol reviews.
6. The final payload review showed only the local directory listing, the synthetic UDP string `lab-udp-exp10`, the query name `localhost`, and ICMP. No credentials or unrelated addresses were retained in the final PCAP.
7. Temporary servers and the dumpcap process were stopped. Ports 18083, 18084, and 15353 were confirmed closed. Promiscuous mode was never enabled, so no mode change required restoration.

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 04:51 +05:30 | GUI window/screenshot tools were unavailable; real PCAP and TShark output are provided instead. |

## Result and cleanup

Result: `PARTIAL`. The final loopback PCAP and protocol analysis are genuine and reviewed, but direct tcpdump capture and Wireshark GUI evidence were unavailable. The final sanitized PCAP may be included because its content was reviewed; discarded broad captures were not retained. Cleanup was verified.

# Experiment 3 — CrypTool 2 cryptanalysis

**Source:** `exp3 cyber.pdf`  
**Status:** `PARTIAL`

## Aim, objectives, and tools

The manual aims to perform basic cryptanalysis and security evaluation using CrypTool 2 and its visualizations. It requires Windows 10/11 64-bit, CrypTool 2, and Microsoft .NET Framework. Required learning components are Caesar Cipher, Playfair Cipher, MD5, SHA, Frequency Test, and Enigma Analyzer.

## Preconditions and safety

Only educational/sample plaintext and ciphertext may be used. MD5 and SHA are one-way hash functions, not reversible encryption. CrypTool-specific results will not be claimed unless CrypTool 2 actually runs.

## Procedure attempted

1. Checked the Linux host for CrypTool executables, Wine, and .NET. Wine and .NET were present, but no CrypTool installer/executable was found and the host is not Windows.
2. Ran the reproducible supplemental Python demonstration in [`supplemental_demo.py`](outputs/supplemental_demo.py) using synthetic text. It performed Caesar shift/decryption, Playfair encryption, frequency counts, MD5, and SHA-256. The real output is [`supplemental-demo.log`](logs/20261012_035200_supplemental-demo.log).
3. Cross-checked file-based MD5/SHA-256 using OpenSSL; output is [`openssl-hashes.log`](logs/20261012_035300_openssl-hashes.log).
4. CrypTool 2's GUI components, especially its Frequency Test and Enigma Analyzer, were not executed. No CrypTool screenshot is claimed.

## Evidence

| Screenshot | Timestamp | What it proves |
|---|---|---|
| None | 2026-10-12 03:53 +05:30 | CrypTool GUI was unavailable; the supplemental terminal demonstration is not CrypTool evidence. |

## Result and cleanup

The supplemental Caesar, Playfair, frequency, MD5, and SHA-256 observations ran successfully on synthetic input. CrypTool 2 itself and Enigma Analyzer were not available, so this is `PARTIAL`, not a completed CrypTool practical. No confidential message or secret was used.

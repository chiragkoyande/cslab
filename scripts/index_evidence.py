#!/usr/bin/env python3
"""
Evidence indexing and checksum verification script for cslab repository.
Generates and verifies evidence/checksums.sha256 and evidence/index.csv.
"""

import os
import glob
import hashlib
import csv
import re
import sys
import argparse
from datetime import datetime

TIMEZONE_SUFFIX = "+05:30"

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def parse_log_metadata(rel_path):
    filename = os.path.basename(rel_path)
    m = re.match(r"^(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})_(.*)\.log$", filename)
    if m:
        year, month, day, hour, minute, second, slug = m.groups()
        iso_time = f"{year}-{month}-{day}T{hour}:{minute}:{second}{TIMEZONE_SUFFIX}"
        clean_slug = slug.replace("-", " ").replace("_", " ")
        desc = f"Log of {clean_slug}"
        # Determine original or derivative
        if any(k in slug for k in ["filter", "reviewed", "final", "summary", "cleaned", "removed"]):
            orig_deriv = "derivative"
        else:
            orig_deriv = "original"
        notes = f"Raw execution log for {slug}"
        return iso_time, desc, orig_deriv, notes
    else:
        # Fallback to mtime
        mtime = datetime.fromtimestamp(os.path.getmtime(rel_path))
        iso_time = mtime.strftime(f"%Y-%m-%dT%H:%M:%S{TIMEZONE_SUFFIX}")
        desc = f"Log file {filename}"
        return iso_time, desc, "original", ""

def parse_output_metadata(rel_path):
    filename = os.path.basename(rel_path)
    # Output file specifics
    known_outputs = {
        "demo.html": ("2026-10-12T03:44:00+05:30", "Benign local HTML demo page for loopback QR demonstration", "derivative", "Served on 127.0.0.1:18082"),
        "demo_qr.png": ("2026-10-12T03:43:00+05:30", "Benign local QR code image targeting 127.0.0.1 demo page", "derivative", "Generated with Python qrcode module"),
        "sample.txt": ("2026-10-12T03:52:00+05:30", "Synthetic input plaintext for cryptographic demonstration", "original", "Educational sample plaintext"),
        "supplemental_demo.py": ("2026-10-12T03:52:00+05:30", "Supplemental Python script for Caesar, Playfair, MD5, and SHA-256", "derivative", "Local substitute for CrypTool 2"),
        "hash.txt": ("2026-10-12T04:05:00+05:30", "Intentionally weak MD5 digest of word password", "original", "Digest: 5f4dcc3b5aa765d61d8327deb882cf99"),
        "wordlist.txt": ("2026-10-12T04:05:00+05:30", "Small synthetic wordlist for dictionary password audit", "original", "6 candidate passwords"),
        "loopback_capture.pcap": ("2026-10-12T04:50:00+05:30", "Sanitized 20-frame loopback packet capture (TCP, UDP, DNS, ICMP)", "derivative", "Filtered from dumpcap capture via editcap; loopback only"),
        "assessment_summary.md": ("2026-10-12T05:10:00+05:30", "Local vulnerability assessment and security compliance summary", "derivative", "Synthesized from local Nmap scan and service state"),
        "vulnerability_report.txt": ("2026-10-12T05:10:00+05:30", "Nmap vulnerability assessment scan report for loopback port 80", "original", "Generated with nmap -sV -sC -p 80 127.0.0.1 -oN"),
    }
    if filename in known_outputs:
        return known_outputs[filename]
    mtime = datetime.fromtimestamp(os.path.getmtime(rel_path))
    iso_time = mtime.strftime(f"%Y-%m-%dT%H:%M:%S{TIMEZONE_SUFFIX}")
    return iso_time, f"Output artifact {filename}", "derivative", ""

def collect_evidence():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    evidence_files = []
    for exp_dir in sorted(glob.glob(os.path.join(repo_root, "experiments", "exp*"))):
        exp_match = re.search(r"exp(\d+)", os.path.basename(exp_dir))
        if not exp_match:
            continue
        exp_id = exp_match.group(1)
        
        # Collect logs
        log_files = sorted(glob.glob(os.path.join(exp_dir, "logs", "*")))
        for idx, f in enumerate(log_files, 1):
            if os.path.isfile(f):
                rel_path = os.path.relpath(f, repo_root)
                ev_id = f"EXP{exp_id}-LOG-{idx:02d}"
                iso_time, desc, orig_deriv, notes = parse_log_metadata(rel_path)
                sha = get_sha256(f)
                evidence_files.append({
                    "experiment_id": exp_id,
                    "evidence_id": ev_id,
                    "timestamp": iso_time,
                    "description": desc,
                    "path": rel_path,
                    "sha256": sha,
                    "original_or_derivative": orig_deriv,
                    "notes": notes
                })

        # Collect outputs
        output_files = sorted(glob.glob(os.path.join(exp_dir, "outputs", "*")))
        for idx, f in enumerate(output_files, 1):
            if os.path.isfile(f):
                rel_path = os.path.relpath(f, repo_root)
                ev_id = f"EXP{exp_id}-OUT-{idx:02d}"
                iso_time, desc, orig_deriv, notes = parse_output_metadata(rel_path)
                sha = get_sha256(f)
                evidence_files.append({
                    "experiment_id": exp_id,
                    "evidence_id": ev_id,
                    "timestamp": iso_time,
                    "description": desc,
                    "path": rel_path,
                    "sha256": sha,
                    "original_or_derivative": orig_deriv,
                    "notes": notes
                })
    return evidence_files

def generate(repo_root):
    evidence = collect_evidence()
    print(f"Collected {len(evidence)} evidence files.")

    # 1. Write evidence/checksums.sha256
    checksum_path = os.path.join(repo_root, "evidence", "checksums.sha256")
    with open(checksum_path, "w", encoding="utf-8") as f:
        f.write("# Generated after evidence capture. Format: SHA256  relative/path\n")
        for item in evidence:
            f.write(f"{item['sha256']}  {item['path']}\n")
    print(f"Wrote checksums to {checksum_path}")

    # 2. Write evidence/index.csv
    index_path = os.path.join(repo_root, "evidence", "index.csv")
    fieldnames = [
        "experiment_id",
        "evidence_id",
        "timestamp",
        "description",
        "path",
        "sha256",
        "original_or_derivative",
        "notes"
    ]
    with open(index_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in evidence:
            writer.writerow(item)
    print(f"Wrote evidence index to {index_path}")

def verify(repo_root):
    checksum_path = os.path.join(repo_root, "evidence", "checksums.sha256")
    if not os.path.exists(checksum_path):
        print(f"Error: {checksum_path} does not exist.")
        sys.exit(1)

    print("Verifying evidence checksums...")
    verified = 0
    errors = 0
    with open(checksum_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue
            expected_sha, rel_path = parts
            full_path = os.path.join(repo_root, rel_path)
            if not os.path.exists(full_path):
                print(f"FAIL (missing): {rel_path}")
                errors += 1
                continue
            actual_sha = get_sha256(full_path)
            if actual_sha.lower() != expected_sha.lower():
                print(f"FAIL (hash mismatch): {rel_path} expected {expected_sha} got {actual_sha}")
                errors += 1
            else:
                verified += 1

    print(f"\nVerification summary: {verified} verified, {errors} errors.")
    if errors > 0:
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Evidence index and checksum tool")
    parser.add_argument("--verify", action="store_true", help="Verify checksums in evidence/checksums.sha256")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if args.verify:
        verify(repo_root)
    else:
        generate(repo_root)
        verify(repo_root)

if __name__ == "__main__":
    main()

# Lab architecture

## Observed host

- Host OS: Fedora Linux 43 Workstation Edition
- Kernel/architecture: Linux 6.17.13-200.fc42.x86_64, x86_64
- Memory: approximately 15 GiB total
- Free space at preflight: approximately 3.6 GiB on `/home`
- Current workspace: `/home/chiragk/Projects/cslab`
- Hypervisor discovery: VirtualBox and VMware commands were not present during preflight
- Local container runtimes discovered: Docker and Podman
- Browser discovered: Firefox

## Approved topology

The safe default is a single-host loopback topology:

```text
local terminal/browser
        |
        | 127.0.0.1 / localhost only
        v
temporary Apache/Python/DVWA/ZAP lab service
```

No service should bind to a public or shared-network interface for these practicals. If a container is used, its published port must bind to `127.0.0.1` and the exact URL must be logged before scanning.

## Limitations

No Kali VM was discovered during the initial host preflight, and no VM snapshot is available to this repository. Firewall experiments therefore require an existing disposable sandbox or remain blocked. Disk space is low enough that large images or package upgrades require explicit review before installation.

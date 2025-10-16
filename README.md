# Simplified-Web-Directory-Brute-Forcer

A minimal, multithreaded directory scanning script for authorized web recon and CTF practice.  
This script issues GET requests to a sequence of paths (e.g. `/0`, `/1`, `/2`…) and prints responses with status code `200`. It is intentionally small and easy to adapt for learning purposes.

> ⚠️ **URGENT DISCLAIMER** Use this script **only** on systems you own, control, or have explicit written permission to test.

---

## What this script does
- Iterates over a numeric range of endpoints (0 … 999 by default)
- Sends concurrent HTTP GET requests using `requests` + `concurrent.futures`
- Prints URLs that return HTTP `200` (can be modified to include other codes)
- Lightweight and easy to customize for simple recon tasks and CTF labs

---

## Requirements
- Python 3.8+  
- `requests` library

Install dependency:
```bash
pip install requests

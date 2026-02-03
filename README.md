# PortBlitz ⚡

**Ultra-fast Async Port Scanner**

```
    ⚡ P O R T B L I T Z ⚡   v1.0
    Ultra-fast Async Port Scanner
```

**Built By:** MIHx0 (Mizaz Haider)  
**Powered By:** The PenTrix

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🚀 Overview

PortBlitz is a high-performance, asynchronous TCP port scanner written in Python. Designed for speed and reliability, it leverages non-blocking I/O to scan thousands of ports in seconds, making it a faster, lightweight alternative to standard threading scanners.

### Key Features (v1.0)
- **⚡ Async Architecture**: Uses Python's `asyncio` for high concurrency (default: 500 threads).
- **🎨 HTML Reporting**: Generates beautiful, self-contained HTML reports for every scan.
- **🛡️ No Dependencies**: Runs on standard Python 3.8+ libraries.
- **🔍 Smart Detection**: Basic service guessing for common ports.

---

## 📥 Installation

```bash
git clone https://github.com/mizazhaider-ceh/portblitz.git
cd portblitz
# No pip install required for v1.0!
```

---

## 💻 Usage

### Basic Scan (Top 1000 Ports)
```bash
python portblitz.py example.com
```

### High Speed Scan (1000 Concurrency)
```bash
python portblitz.py 192.168.1.1 -c 1000
```

### Specific Port Range
```bash
python portblitz.py example.com -p 1-5000
python portblitz.py example.com -p 80,443,8080
```

### All Ports (1-65535)
```bash
python portblitz.py example.com -p all
```

---

## 📊 Roadmap

We have an exciting roadmap ahead!

- **v1.0** (Current): Async TCP scanning, HTML reports.
- **v2.0**: Service version detection & Banner grabbing.
- **v3.0**: CIDR range scanning & `uvloop` support.
- **v4.0**: Script Engine (vulnerability checks).
- **v5.0**: Interactive TUI Dashboard.

See [roadmap.md](roadmap.md) for full details.

---

## ⚠️ Legal Disclaimer

For authorized security testing and educational purposes only. The authors are not responsible for unauthorized use.

---

**Built with 💻 & ☕ by MIHx0**

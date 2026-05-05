# Network Port Scanner 🔍

A Python-based tool to scan open ports of a target system using socket programming.

## 🛠️ Tools Used
- Python
- socket (built-in library)

## ✨ Features
- Scans 9 most common ports
- Identifies open ports and their services
- Detects high-risk ports (SMB, MySQL, RDP etc.)
- Works on any IP or hostname

## ▶️ How to Run

```bash
python simple_port_scanner.py
```

## 📌 Sample Output
Enter target IP or hostname: scanme.nmap.org
Scanning target: 45.33.32.156
Port    80  |  OPEN  |  HTTP
Port   443  |  OPEN  |  HTTPS
Scan complete. 2 open port(s) found.
## 🔍 How It Works
1. Takes target IP or hostname as input
2. Resolves hostname to IP using socket.gethostbyname()
3. Tries TCP connection on each port using socket.connect_ex()
4. If return value is 0 → port is OPEN
5. Displays open ports with their service names

## ⚠️ Disclaimer
This tool is for educational purposes only.
Only scan systems you have permission to scan.

## 👩‍💻 Author
**Divyanshi Rana**
BTech CSE | Banasthali Vidyapith

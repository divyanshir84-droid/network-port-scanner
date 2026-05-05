# ================================================
# Network Port Scanner
# Author: Divyanshi Rana
# Tools Used: Python, socket library
# ================================================

import socket

# ── Step 1: Take target from user ───────────────
target = input("Enter target IP or hostname: ")

# ── Step 2: Resolve hostname to IP ──────────────
ip = socket.gethostbyname(target)
print("\nScanning target:", ip)
print("-" * 40)

# ── Step 3: Common ports and their services ──────
services = {
    21:   "FTP",
    22:   "SSH",
    23:   "Telnet",
    80:   "HTTP",
    443:  "HTTPS",
    445:  "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt",
}

open_ports = []

# ── Step 4: Scan each port ───────────────────────
for port in services:

    # Create a new socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout so it doesn't wait too long
    s.settimeout(1)

    # Try to connect — returns 0 if port is open
    result = s.connect_ex((ip, port))

    if result == 0:
        service = services[port]
        print(f"Port {port:5}  |  OPEN  |  {service}")
        open_ports.append(port)

    # Close socket after each check
    s.close()

# ── Step 5: Summary ──────────────────────────────
print("-" * 40)
print(f"Scan complete. {len(open_ports)} open port(s) found.")
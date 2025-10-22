# PortAuditor: A Simple Python Network Port Scanner

## 💡 Overview

**PortAuditor** is a foundational TCP port scanner developed in Python. Designed to quickly identify open ports on single or multiple target hosts, this tool provides clear, color-coded output for immediate visibility into network service availability.

This project demonstrates core skills in network socket programming, basic command-line tool design, and Python proficiency, serving as a strong foundation for further cybersecurity and networking tool development.

## 🛠️ Key Features & Skills Demonstrated

* **Network Programming:** Utilizes the Python `socket` library to establish TCP connections, effectively checking port status.
* **Multiple Target Support:** Designed to handle multiple target IP addresses, separated by commas, entered by the user.
* **Intuitive CLI:** Basic Command Line Interface (CLI) for simple execution and user interaction.
* **Enhanced User Experience:** Implements the `termcolor` library to provide clear, **color-coded output** for easy reading of results.
* **Core Python Proficiency:** Strong application of functions, loops, and exception handling (`try...except`) to manage connection failures.

## 🚀 How to Use

### Prerequisites
You need to install the `termcolor` library in your Python environment:


```

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AgilAliyev1/PSA.git
   cd PSA
   ```

2. **Install required dependencies:**
   ```bash
   pip install termcolor
   ```

3. **Run the port scanner:**
   ```bash
   python portscanner.py
   ```

## 📋 Example Usage

### Single Target Scan
```bash
[*] Enter Target to Scan(Split them by ,) : 192.168.1.1
[*] Enter How Many Ports You Want To Scan: 100

Scanning: 192.168.1.1
[+] Port Opened 22
[+] Port Opened 80
[+] Port Opened 443
```

### Multiple Target Scan
```bash
[*] Enter Target to Scan(Split them by ,) : 192.168.1.1, 192.168.1.2, 192.168.1.3
[*] Enter How Many Ports You Want To Scan: 50

[*] Scanning Multiple Targets
Scanning: 192.168.1.1
[+] Port Opened 22
[+] Port Opened 80

Scanning: 192.168.1.2
[+] Port Opened 22

Scanning: 192.168.1.3
[+] Port Opened 80
[+] Port Opened 443
```

## 🔗 Repository
Visit the project repository: [https://github.com/AgilAliyev1/PSA](https://github.com/AgilAliyev1/PSA)
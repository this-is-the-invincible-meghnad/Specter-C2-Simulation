# 🛡️ Specter-C2: Persistent Remote Access Simulation

**Specter-C2** is an advanced Python-based Remote Access Trojan (RAT) simulation developed for Module 07: Malware Threats. This project demonstrates the architecture of modern persistent threats, focusing on stealth, survival, and remote command execution [cite: 2026-02-14].

## 🚀 Key Features

| Requirement | Implementation | Status |
| :--- | :--- | :--- |
| **Persistence** | Windows Registry 'Run' key injection (`winreg`) [cite: 2026-02-14] | ✅ Active |
| **Stealth** | Background processing via `pythonw` [cite: 2026-02-14] | ✅ Active |
| **Remote Access** | Reverse-TCP Command & Control (C2) [cite: 2026-02-14] | ✅ Active |
| **Resilience** | Automated re-connection logic [cite: 2026-02-14] | ✅ Active |

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/this-is-the-invincible-meghnad/Specter-C2-Simulation](https://github.com/this-is-the-invincible-meghnad/Specter-C2-Simulation)
cd Specter-C2-Simulation
```
### Install Dependencies 
 ```bash
 pip install -requirements.txt
 ```
 ### 🧪 Simulation Options
Option A: Automated Lab (Recommended for Recruiters) ⚡
To witness the C2 interaction without manual VM configuration, use the containerized environment [cite: 2026-02-14]:
 ```bash
 docker-compose up --build
 ```
 This launches both the Attacker (C2) and Victim (Payload) in isolated containers for immediate review [cite: 2026-02-14].

 ### Option B: Manual Research Environment (Step-by-Step) 💻
* Attacker: Run python Specture_c2.py on the host machine [cite: 2026-02-14].
* Victim: Move Specture_Payload.py to a Windows VM and execute via pythonw Specture_Payload.py [cite: 2026-02-14].
* Persistence Test: Restart the VM. The payload will automatically re-establish the connection to the C2 upon reboot [cite: 2026-02-14].
### 📂 Project Structure
* Specture_c2.py: The Attacker's command station (Listener) [cite: 2026-02-14].
* Specture_Payload.py: The Victim's background process (Target) [cite: 2026-02-14].
* requirements.txt: Environment configuration file [cite: 2026-02-14].
* docker-compose.yml: Automated lab environment for quick simulation [cite: 2026-02-14].
### ⚠️ Disclaimer
This tool is for educational and ethical security research only. Unauthorized use on systems you do not own is strictly prohibited and illegal [cite: 2026-02-14].
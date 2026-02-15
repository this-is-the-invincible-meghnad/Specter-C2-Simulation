# 🛡️ Specter-C2: Persistent Remote Access Simulation

**Specter-C2** is an advanced Python-based Remote Access Trojan (RAT) simulation developed for Module 07: Malware Threats. This project demonstrates the architecture of modern persistent threats, focusing on stealth, survival, and remote command execution

## 🚀 Key Features

| Requirement | Implementation | Status |
| :--- | :--- | :--- |
| **Persistence** | Windows Registry 'Run' key injection (`winreg`) | ✅ Active |
| **Stealth** | Background processing via `python`  | ✅ Active |
| **Remote Access** | Reverse-TCP Command & Control (C2) | ✅ Active |
| **Resilience** | Automated re-connection logic | ✅ Active |

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
To witness the C2 interaction without manual VM configuration, use the containerized environment
 ```bash
 docker-compose up --build
 ```
 This launches both the Attacker (C2) and Victim (Payload) in isolated containers for immediate review 

 ## Option B: Manual Research Environment (Step-by-Step) 💻
* Attacker: Run python Specture_c2.py on the host machine
* Victim: Move Specture_Payload.py to a Windows VM and execute via pythonw Specture_Payload.py
* Persistence Test: Restart the VM. The payload will automatically re-establish the connection to the C2 upon reboot
### 📂 Project Structure
* Specture_c2.py: The Attacker's command station (Listener)
* Specture_Payload.py: The Victim's background process (Target) 
* requirements.txt: Environment configuration file 
* docker-compose.yml: Automated lab environment for quick simulation 
### ⚠️ Disclaimer
This tool is for educational and ethical security research only. Unauthorized use on systems you do not own is strictly prohibited and illegal 
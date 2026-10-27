# Python Network Automation Toolkit
### Official Companion Scripts for Cisco Certification Master Study Handbook

This directory contains ready-to-run Python automation scripts demonstrating production workflows referenced in:
- **CCNA (Chapter 6):** Automation & Programmability, REST APIs, JSON parsing
- **CCNP ENCOR (Chapter 11):** Netmiko SSH execution, EEM Python automation, RESTCONF and YANG data models
- **CCNP ENARSI (Chapters 12 & 14):** BGP neighbor state inspection and infrastructure telemetry

---

## 🛠️ Setup Instructions

### 1. Create a Python Virtual Environment
```bash
# Navigate to the automation-scripts directory
cd automation-scripts

# Create virtual environment
python -m venv venv

# Activate on Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Activate on Linux/macOS:
source venv/bin/activate
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 📜 Script Index

| Script File | Purpose | Relevant Book Chapter |
|:---|:---|:---|
| `01_backup_running_config_netmiko.py` | Automated multi-device timestamped backup via SSH/Netmiko | Chapter 11 (Section 11.1) |
| `02_bulk_vlan_provisioning_netmiko.py` | Bulk campus VLAN configuration and NVRAM saving | Chapter 2 & Chapter 11 |
| `03_restconf_interface_telemetry_requests.py` | Retrieves operational interface telemetry via RESTCONF & YANG | Chapter 6 & Chapter 11 |
| `04_restconf_configure_loopback.py` | Provisions Loopback interfaces using RESTCONF PUT requests | Chapter 6 (Section 6.2) |
| `05_napalm_bgp_and_facts_audit.py` | Gathers hardware facts and audits BGP neighbor peering states | Chapter 8 & Chapter 12 |

---

## ⚙️ Device Prerequisites on Cisco IOS-XE
Ensure your lab router or switch has SSH and RESTCONF enabled:
```cisco
! Enable SSH & Local AAA
username admin privilege 15 secret Cisco123!
ip domain-name lab.local
crypto key generate rsa general-keys modulus 2048
line vty 0 4
 transport input ssh
 login local

! Enable RESTCONF (YANG over HTTPS Port 443)
ip http secure-server
restconf
```

# Cisco Certification Master Study Handbook
## Official Companion Repository, Errata Tracker & Lab Archive

[![Book Edition](https://img.shields.io/badge/Edition-First%20Edition%202026-blue.svg)](https://github.com/adarsh-panicker/cisco-certification-master-handbook)
[![Certifications](https://img.shields.io/badge/Cisco%20Tracks-CCNA%20|%20ENCOR%20|%20ENARSI-green.svg)](https://github.com/adarsh-panicker/cisco-certification-master-handbook)
[![Author](https://img.shields.io/badge/Author-Adarsh%20Panicker-orange.svg)](https://github.com/adarsh-panicker)
[![License](https://img.shields.io/badge/License-MIT%20/%20Educational-purple.svg)](LICENSE)

Welcome to the official companion repository for the **Cisco Certification Master Study Handbook** (First Edition, 2026) by **Adarsh Panicker**.

This repository hosts official lab files, configuration templates, Python network automation scripts, high-resolution reference materials, and the continuously maintained **Errata & Blueprint Changelog**.

---

## 📚 About the Handbook

A unified, multi-tier engineering handbook designed for network engineers and IT infrastructure professionals studying for:
- **CCNA (200-301 v1.1)** — Chapters 1 to 6 & Master Lab 1
- **CCNP Enterprise Core ENCOR (350-401 v1.1)** — Chapters 7 to 11 & Master Lab 2
- **CCNP Enterprise Advanced Routing ENARSI (300-410 v1.1)** — Chapters 12 to 14, Protocol Matrix & Master Lab 3

Key book statistics:
- **14 Chapters & 66 Technical Lessons**
- **133 High-Resolution Architecture Schematics & CLI Capture Cards**
- **130 Practice Exam Questions (70 In-Chapter + 60 Mock Exam)**
- **3 Master Hands-On Labs with End-to-End Verification**
- **Master 14-Page Technical Glossary & Production Command Cheat Sheets**

---

## 🗂️ Companion Repository Contents

```text
├── labs/
│   ├── ccna/                   # Cisco Packet Tracer (.pkt) initial configs & lab exercises
│   ├── encor/                  # Multi-VLAN, Dual HSRP, LACP, and Multi-Area OSPF topologies
│   └── enarsi/                 # Advanced OSPF/EIGRP redistribution, BGP peering, DMVPN configs
├── topologies-cml-eveng/       # Cisco Modeling Labs (CML 2.x) & EVE-NG YAML topologies & startup configs
├── automation-scripts/         # Chapter 11 Python Netmiko, Requests, and RESTCONF automation toolkit
├── cheat-sheets/               # Printable Subnetting, OSPF LSA, BGP 13-Step & Command Cheat Sheets
├── anki-flashcards/            # 400+ Interactive Spaced-Repetition Anki Flashcards (CSV & TXT)
├── ERRATA.md                   # Continuous Errata Tracker and Blueprint update changelog
└── .github/                    # Official Issue submission templates for reader feedback
```

---

## 🎁 Bonus Companion Resources & Downloads

### 1. [Cisco Packet Tracer Lab Archives (.pkt & configs)](labs/ccna/)
Pre-built, validated switch and router configurations matching every Part I CCNA configuration exercise and worked scenario walkthrough in this book:
- `lab1_vlan_8021q_trunking.cfg`: 802.1Q trunking, access ports, and LACP EtherChannel bundles.
- `lab2_router_on_a_stick.cfg`: Subinterfaces dot1Q encapsulation and DHCP relay helper.
- `lab3_ospfv2_single_area.cfg`: Single-Area OSPFv2 routing and passive interface tuning.
- `lab4_pat_overload_nat.cfg`: Dynamic Port Address Translation (PAT) overload configuration.
- `lab5_port_security_dhcp_snooping.cfg`: Layer 2 switch defense, sticky MAC security, and DHCP snooping trust.

### 2. [Cisco Modeling Labs (CML) & EVE-NG Topologies (.yaml)](topologies-cml-eveng/)
Importable multi-node network topologies for ENCOR and ENARSI labs, including startup configuration files:
- `cml_encor_master_lab_ha_hsrp_ospf.yaml`: Dual HSRP v2 with IP SLA object tracking, LACP EtherChannel, and Multi-Area OSPF.
- `cml_enarsi_master_lab_redistribution_pbr.yaml`: Mutual OSPF-to-EIGRP redistribution, route-map tagging, prefix-list filtering, and Policy-Based Routing.
- `eve_ng_dmvpn_phase3_bgp.unl.yaml`: Dual-hub DMVPN Phase 3 with NHRP shortcut and iBGP peering.

### 3. [Python Network Automation Toolkit](automation-scripts/)
Production-grade Python automation scripts utilizing **Netmiko**, **Requests**, and **NAPALM**:
- `01_backup_running_config_netmiko.py`: Automated multi-device timestamped running-config backups.
- `02_bulk_vlan_provisioning_netmiko.py`: Automated multi-switch VLAN provisioning and NVRAM saving.
- `03_restconf_interface_telemetry_requests.py`: RESTCONF GET request retrieving operational state via `ietf-interfaces` YANG JSON.
- `04_restconf_configure_loopback.py`: RESTCONF PUT request provisioning Loopback interfaces.
- `05_napalm_bgp_and_facts_audit.py`: Multi-vendor audit of device facts, serial numbers, and BGP neighbor peering states.

### 4. [Printable High-Resolution Cheat Sheets](cheat-sheets/)
Laminated-ready quick-reference cheat sheets:
- `01_IPv4_Subnetting_VLSM_and_Wildcard_Cheat_Sheet.md`: Prefixes /8 to /32, block sizes, and 3-step rapid mental math.
- `02_OSPF_LSA_Types_and_Area_Rules_Cheat_Sheet.md`: LSA Types 1 to 7, stub rules, and adjacency parameters.
- `03_BGP_13_Step_Path_Selection_Algorithm_Cheat_Sheet.md`: Complete 13-step best-path selection flow and mnemonics.
- `04_Administrative_Distance_and_Well_Known_Ports_Cheat_Sheet.md`: AD rankings (0-255) and over 20 critical Cisco ports.
- `05_Cisco_IOS_XE_Master_Diagnostic_Commands_Cheat_Sheet.md`: Essential show commands for Switching, Routing, and Security.

### 5. [Interactive Anki Flashcard Decks](anki-flashcards/)
Over 400 digital spaced-repetition flashcards covering:
- Every term in the Master 14-Page Glossary categorized by track ([A] CCNA, [E] CCNP ENCOR, [R] CCNP ENARSI).
- Administrative Distance and Protocol Timer defaults (OSPF, EIGRP, BGP, HSRP, VRRP, STP).
- All 70 Chapter Practice Questions and 60 Mock Exam Questions with detailed rationales.
- Production Pro-Tips and real-world field traps.

---

## 📝 Errata, Updates, and Reader Feedback

Cisco certification blueprints and Cisco IOS-XE software versions evolve over time. While every CLI snippet, configuration walkthrough, subnetting calculation, and protocol explanation has been rigorously lab-tested, minor errata or command syntax shifts may occur.

- **Review Existing Errata**: Check [ERRATA.md](ERRATA.md) for verified corrections and blueprint changelogs.
- **Submit Errata or Feedback**: Open a new issue using our [GitHub Issues Page](https://github.com/adarsh-panicker/cisco-certification-master-handbook/issues/new).

When submitting an errata report, please include:
1. **Book Title & Edition** (First Edition, 2026)
2. **Chapter Number & Section Heading** (e.g. Chapter 3, Section 3.2)
3. **Exact Text or CLI Snippet in Question**
4. **Your Suggested Correction or Observation**

---

## 👨‍💻 About the Author

**Adarsh Panicker** is an IT infrastructure professional with more than 13 years of enterprise experience, over 10 of them in the GCC region, including Qatar. His hands-on background spans enterprise Cisco routing and switching, Windows Server, Active Directory Domain Services, Hyper-V, enterprise next-generation firewalls (SonicWall and Fortinet), Microsoft 365, Entra ID hybrid synchronization, Microsoft Intune, Azure disaster recovery, Linux infrastructure, and enterprise monitoring with Zabbix.

He holds a Bachelor of Science in Computer Science and a diploma in computer hardware and networking, along with Google IT Support Professional, IBM Cybersecurity Analyst, IBM Data Analyst, Python, C#, Responsive web design, Ethical hacking with open source tools, and ITIL 4 Foundation certifications.

- **GitHub Profile**: [github.com/adarsh-panicker](https://github.com/adarsh-panicker/)
- **Companion Repository**: [github.com/adarsh-panicker/cisco-certification-master-handbook](https://github.com/adarsh-panicker/cisco-certification-master-handbook)

# Cisco Modeling Labs (CML) & EVE-NG Lab Topologies
### Official Multi-Node Virtual Topologies for CCNP ENCOR & ENARSI Master Labs

This directory contains importable network topology definitions and verified Cisco IOS-XE initial configurations matching the Master Labs in the **Cisco Certification Master Study Handbook**.

---

## 📁 Files Included

| Topology File | Platform | Primary Book Lab Covered |
|:---|:---|:---|
| `cml_encor_master_lab_ha_hsrp_ospf.yaml` | Cisco Modeling Labs 2.x | Part II ENCOR Master Lab (Dual HSRP, LACP, Multi-Area OSPF) |
| `cml_enarsi_master_lab_redistribution_pbr.yaml` | Cisco Modeling Labs 2.x | Part III ENARSI Master Lab (Redistribution, Tagging, PBR) |
| `eve_ng_dmvpn_phase3_bgp.unl.yaml` | EVE-NG / GNS3 | Chapter 13 (DMVPN Phase 3 with NHRP Shortcut & iBGP) |

### Node Startup Configurations (`configs/`)
- `DSW1_ENCOR_initial.cfg`: Primary Active HSRP gateway with IP SLA tracking probe.
- `DSW2_ENCOR_initial.cfg`: Standby HSRP gateway and LACP channel-group partner.
- `R1_ENARSI_redistribution.cfg`: Mutual OSPF/EIGRP redistribution gateway with route-map tagging.
- `R2_ENARSI_ospf_core.cfg`: Multi-Area OSPF backbone core router.
- `R3_ENARSI_pbr_edge.cfg`: Policy-Based Routing edge router with route-map traffic diverters.

---

## 🚀 Import Instructions

### For Cisco Modeling Labs (CML 2.x):
1. Log into your CML web user interface.
2. Click **Import** on the main dashboard.
3. Select either `cml_encor_master_lab_ha_hsrp_ospf.yaml` or `cml_enarsi_master_lab_redistribution_pbr.yaml`.
4. Click **Import Lab**.
5. Start nodes and paste the corresponding startup configuration from the `configs/` folder into each node console.

### For EVE-NG / GNS3:
1. Copy the node configurations into your virtual router instances (e.g. `c8000v` or `IOL`).
2. Interconnect interfaces according to the labels defined in the `.yaml` topology schematic.
3. Boot nodes and verify using verification commands detailed in Chapter 7 and Chapter 12.

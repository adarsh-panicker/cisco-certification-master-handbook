# Cisco Packet Tracer Lab Topologies & Configurations
### Official Part I CCNA (200-301) Hands-On Lab Guides

This directory contains pre-configured, tested Cisco IOS-XE configuration templates matching every primary lab scenario in **Part I (CCNA)** of the *Cisco Certification Master Study Handbook*.

---

## 🧪 Included Lab Guides (`configs/`)

| Lab File | Focus Area | Key Commands & Concepts Verified | Book Chapter |
|:---|:---|:---|:---|
| `lab1_vlan_8021q_trunking.cfg` | Switching & EtherChannel | `switchport mode trunk`, `channel-group 1 mode active`, `spanning-tree portfast` | Chapter 2 |
| `lab2_router_on_a_stick.cfg` | Inter-VLAN Routing | `encapsulation dot1Q`, subinterfaces, `ip helper-address`, DHCP pools | Chapter 2 |
| `lab3_ospfv2_single_area.cfg` | Layer 3 Routing | `router ospf 1`, `network ... area 0`, `passive-interface`, OSPF timers | Chapter 3 |
| `lab4_pat_overload_nat.cfg` | IP Services & NAT | `ip nat inside`, `ip nat outside`, `ip nat inside source list ... overload` | Chapter 4 |
| `lab5_port_security_dhcp_snooping.cfg` | Layer 2 Switch Hardening | `switchport port-security mac-address sticky`, `ip dhcp snooping trust` | Chapter 5 |

---

## 🛠️ How to Build These Labs in Cisco Packet Tracer

1. Open Cisco Packet Tracer (v8.2 or later).
2. Deploy the recommended devices:
   - **Routers**: Cisco 2911 or 4321 / 4331 series.
   - **Switches**: Cisco Catalyst 2960-24TT or 3650 / 3560 Multilayer switches.
3. Cable the topology according to the interface descriptions in the `.cfg` files.
4. Click on each device -> Navigate to the **CLI** tab -> Paste the configuration.
5. Verify operational status using:
   - `show ip interface brief`
   - `show vlan brief`
   - `show etherchannel summary`
   - `show ip route`
   - `show ip nat translations`
   - `show port-security interface ...`

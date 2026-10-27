# Cisco IOS-XE Master Diagnostic Commands Cheat Sheet
### Essential CLI Show Commands for CCNA, ENCOR & ENARSI Examinations

---

## 🔍 1. General Interface & System Health
```cisco
show ip interface brief              ! Quick summary of interface IP and up/up status
show interfaces status               ! Switchport speed, duplex, VLAN, and negotiation
show interfaces transceiver          ! Optical power levels, dBm Rx/Tx for fiber SFP/SFP+
show version                         ! Uptime, IOS-XE image version, serial, license level
show platform software status control-processor brief ! CPU utilization per core
show processes cpu sorted | exclude 0.00%             ! Top CPU consuming processes
show environment                     ! Power supplies, fan speed, internal temperatures
```

## 🔄 2. Switching, VLANs, STP & EtherChannel
```cisco
show vlan brief                      ! Active VLANs and assigned access switchports
show interfaces trunk                ! Active 802.1Q trunks, native VLAN, allowed list
show spanning-tree                   ! STP root bridge ID, local priority, port roles/states
show spanning-tree summary           ! PortFast, BPDU Guard, and MST instance overview
show etherchannel summary            ! LACP/PAgP bundle status (SU = Layer 2 In-Use, RU = L3)
show mac address-table dynamic       ! Learned dynamic MAC addresses and egress ports
show cdp neighbors detail            ! Cisco discovery: neighbor IP, platform, capabilities
show lldp neighbors detail           ! IEEE standard neighbor discovery details
```

## 🌐 3. IP Routing & Protocol Diagnostics
```cisco
show ip route                        ! Full Routing Information Base (RIB)
show ip route [prefix]               ! Detailed inspection of route source, metric, AD
show ip protocols                    ! Active routing processes, timers, passive interfaces
show ip ospf neighbor                ! OSPF neighbor states (FULL, 2WAY, INIT)
show ip ospf database                ! OSPF Link-State Database (LSDB) Type 1-5 LSAs
show ip ospf interface brief         ! OSPF area, network type, cost, and DR/BDR roles
show ip eigrp neighbors              ! EIGRP neighbor uptime, SRTT, RTO, Q-count
show ip eigrp topology               ! EIGRP Feasible Successors and Feasibility Condition
show ip bgp summary                  ! BGP neighbor status, AS, prefixes received
show ip bgp                          ! BGP table, path attributes, Best Path (*) indicators
```

## 🛡️ 4. Security, First-Hop Redundancy & Services
```cisco
show standby brief                   ! HSRP active/standby state, virtual IP, priority
show vrrp brief                      ! VRRP master/backup status
show glbp brief                      ! GLBP AVG and AVF forwarder states
show ip nat translations             ! Active NAT/PAT translation table
show ip nat statistics               ! NAT pool allocation, hits, misses, expired translations
show ip dhcp snooping binding        ! Dynamic IP-to-MAC-to-VLAN-to-Port binding database
show port-security interface [int]   ! Violation counts, secure MACs, operational action
show crypto ikev2 sa                 ! FlexVPN / IPsec Phase 1 IKEv2 security associations
show crypto ipsec sa                 ! IPsec Phase 2 Encapsulating Security Payload (ESP)
```

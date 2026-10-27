# Administrative Distance & Well-Known Ports Cheat Sheet
### Cisco Certification Master Study Handbook — Quick Reference Series

---

## 🧭 1. Cisco IOS-XE Administrative Distance (AD) Hierarchy

Administrative Distance measures route believability (0 = most trusted, 255 = untrusted / not installed).

| Route Source | Default AD | Architectural Notes |
|:---|:---:|:---|
| **Directly Connected Interface** | **0** | Active link with IP configured |
| **Static Route** | **1** | Pointed to next-hop IP or egress interface |
| **EIGRP Summary Route** | **5** | Locally generated summary route (`ip summary-address`) |
| **External BGP (eBGP)** | **20** | Routes received from external Autonomous Systems |
| **EIGRP Internal** | **90** | Standard intra-AS EIGRP routes |
| **OSPF** | **110** | Intra-area, Inter-area, and External (E1/E2/N1/N2) |
| **IS-IS** | **115** | Intermediate System to Intermediate System |
| **RIP** | **120** | Routing Information Protocol (v1 & v2) |
| **EIGRP External** | **170** | Routes redistributed into EIGRP |
| **Internal BGP (iBGP)** | **200** | BGP routes learned from intra-AS peers |
| **DHCP Default Gateway** | **254** | Default route learned via DHCP client interface |
| **Untrusted / Unknown** | **255** | Never installed in the Routing Information Base (RIB) |

---

## 🔌 2. Critical Cisco Certification Port Numbers

| Service / Protocol | Protocol | Default Port | Certification Focus |
|:---|:---:|:---:|:---|
| **FTP Data / Control** | TCP | 20 / 21 | File transfer |
| **SSH** | TCP | 22 | Secure remote device administration |
| **Telnet** | TCP | 23 | Insecure legacy management (Must disable) |
| **TACACS+** | TCP | 49 | Cisco AAA (Separates Auth, Authz, Acct) |
| **DNS** | UDP / TCP | 53 | Domain name resolution |
| **DHCP Server / Client** | UDP | 67 / 68 | IPv4 dynamic address allocation |
| **TFTP** | UDP | 69 | Trivial file transfer (UDP based) |
| **HTTP / HTTPS** | TCP | 80 / 443 | Web access / RESTCONF |
| **NTP** | UDP | 123 | Network Time Protocol (Stratum hierarchy) |
| **SNMP Query / Trap** | UDP | 161 / 162 | Network monitoring and traps |
| **BGP** | TCP | 179 | Exterior Gateway Protocol peering |
| **RADIUS Auth / Acct** | UDP | 1812 / 1813 | IETF AAA standard (1645/1646 legacy) |
| **IPsec IKE / NAT-T** | UDP | 500 / 4500 | Internet Key Exchange & NAT Traversal |
| **DHCPv6 Client / Server**| UDP | 546 / 547 | IPv6 address configuration |
| **NETCONF** | TCP | 830 | Network Configuration Protocol (YANG over SSH)|
| **LISP Control / Data** | UDP | 4342 / 4341 | Location/ID Separation Protocol |
| **VXLAN** | UDP | 4789 | Virtual Extensible LAN data encapsulation |
| **CAPWAP Control / Data** | UDP | 5246 / 5247 | Controller-Based Wireless AP communication |
| **gRPC Telemetry** | TCP | 57400 | Streaming network telemetry |

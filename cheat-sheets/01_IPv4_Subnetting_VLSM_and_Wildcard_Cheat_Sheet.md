# IPv4 Subnetting, VLSM & Wildcard Mask Cheat Sheet
### Cisco Certification Master Study Handbook — Quick Reference Series

---

## 🧮 1. Complete Prefix Length, Subnet Mask & Host Capacity Table

| Prefix | Subnet Mask | Wildcard Mask | Total IPs | Usable Hosts ($2^H - 2$) | Block Size (Magic Number) | Classful Scope |
|:---|:---|:---|:---|:---|:---|:---|
| **/32** | 255.255.255.255 | 0.0.0.0 | 1 | 1 (Host Route / Loopback) | 1 | Single Host |
| **/31** | 255.255.255.254 | 0.0.0.1 | 2 | 2 (RFC 3021 Point-to-Point) | 2 | P2P WAN |
| **/30** | 255.255.255.252 | 0.0.0.3 | 4 | 2 (Traditional P2P Link) | 4 | Traditional P2P |
| **/29** | 255.255.255.248 | 0.0.0.7 | 8 | 6 | 8 | Small DMZ / Firewall |
| **/28** | 255.255.255.240 | 0.0.0.15 | 16 | 14 | 16 | Small Office |
| **/27** | 255.255.255.224 | 0.0.0.31 | 32 | 30 | 32 | Department / Branch |
| **/26** | 255.255.255.192 | 0.0.0.63 | 64 | 62 | 64 | Server Farm / Building |
| **/25** | 255.255.255.128 | 0.0.0.127 | 128 | 126 | 128 | Half Class C |
| **/24** | 255.255.255.0 | 0.0.0.255 | 256 | 254 | 1 (in 3rd octet) | Full Class C |
| **/23** | 255.255.254.0 | 0.0.1.255 | 512 | 510 | 2 (in 3rd octet) | Medium Enterprise |
| **/22** | 255.255.252.0 | 0.0.3.255 | 1,024 | 1,022 | 4 (in 3rd octet) | Large Campus |
| **/21** | 255.255.248.0 | 0.0.7.255 | 2,048 | 2,046 | 8 (in 3rd octet) | Aggregated Site |
| **/20** | 255.255.240.0 | 0.0.15.255 | 4,096 | 4,094 | 16 (in 3rd octet) | Regional Hub |
| **/19** | 255.255.224.0 | 0.0.31.255 | 8,192 | 8,190 | 32 (in 3rd octet) | Metro Distribution |
| **/18** | 255.255.192.0 | 0.0.63.255 | 16,384 | 16,382 | 64 (in 3rd octet) | Data Center Fabric |
| **/17** | 255.255.128.0 | 0.0.127.255 | 32,768 | 32,766 | 128 (in 3rd octet) | Large Metro Core |
| **/16** | 255.255.0.0 | 0.0.255.255 | 65,536 | 65,534 | 1 (in 2nd octet) | Full Class B |
| **/8** | 255.0.0.0 | 0.255.255.255 | 16,777,216 | 16,777,214 | 1 (in 1st octet) | Full Class A |

---

## ⚡ 2. The 3-Step Rapid Subnetting Formula (Mental Math)

To find Subnet ID, First Host, Last Host, and Broadcast Address in under 15 seconds:

1. **Find the Interesting Octet:**
   - Prefix `/1` to `/8` $\rightarrow$ 1st octet
   - Prefix `/9` to `/16` $\rightarrow$ 2nd octet
   - Prefix `/17` to `/24` $\rightarrow$ 3rd octet
   - Prefix `/25` to `/32` $\rightarrow$ 4th octet

2. **Calculate the Block Size (Magic Number):**
   $$\text{Block Size} = 256 - \text{Subnet Mask in Interesting Octet}$$
   *(Example for `/27` ($255.255.255.224$): Block size $= 256 - 224 = 32$)*

3. **Find the Nearest Multiple:**
   - Multiples of 32: $0, 32, 64, 96, 128, 160, 192, 224$.
   - For IP `192.168.1.170/27`: 170 falls between 160 and 192.
   - **Subnet ID:** `192.168.1.160`
   - **First Usable Host:** `192.168.1.161`
   - **Last Usable Host:** `192.168.1.190`
   - **Broadcast Address:** `192.168.1.191`

---

## 🔒 3. Private IPv4 Address Allocations (RFC 1918)
- **Class A Private:** `10.0.0.0/8` (`10.0.0.0` to `10.255.255.255`)
- **Class B Private:** `172.16.0.0/12` (`172.16.0.0` to `172.31.255.255`)
- **Class C Private:** `192.168.0.0/16` (`192.168.0.0` to `192.168.255.255`)
- **APIPA / Link-Local:** `169.254.0.0/16` (`169.254.0.0` to `169.254.255.255`)
- **Loopback:** `127.0.0.0/8` (`127.0.0.1` to `127.255.255.254`)

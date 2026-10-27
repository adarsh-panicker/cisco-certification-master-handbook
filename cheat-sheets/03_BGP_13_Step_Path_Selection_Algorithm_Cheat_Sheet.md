# BGP 13-Step Best Path Selection Algorithm
### Cisco Certification Master Study Handbook — Quick Reference Series

BGP evaluates candidate routes sequentially until a single tie-breaker selects the best path.

---

## 🎯 The 13 Decision Steps in Strict Order of Precedence

```text
       ┌────────────────────────────────────────────────────────┐
       │ Step 0: Check Next-Hop Reachability (FIB must resolve) │
       └─────────────────────────┬──────────────────────────────┘
                                 ▼
┌──────┬─────────────────────────┬──────────────────────┬─────────────────────────────┐
│ Step │ Attribute / Metric      │ Selection Criterion  │ Scope & Default Value       │
├──────┼─────────────────────────┼──────────────────────┼─────────────────────────────┤
│  1   │ Weight                  │ Highest Weight wins  │ Cisco-proprietary, Local, 0 │
│      │                         │                      │ (32768 for locally-injected)│
│  2   │ Local Preference        │ Highest Local-Pref   │ AS-wide, Default: 100       │
│  3   │ Locally Originated      │ Local routes preferred│ network / aggregate / redst│
│  4   │ AS_PATH Length          │ Shortest AS_PATH     │ Global (AS prepend adds)    │
│  5   │ Origin Code             │ Lowest Origin Code   │ IGP (i) < EGP (e) < ? (inc) │
│  6   │ MED (Multi-Exit Disc.)  │ Lowest MED wins      │ Between adjacent ASes, 0    │
│  7   │ Neighbor Type           │ eBGP over iBGP       │ External paths favored      │
│  8   │ IGP Metric to Next-Hop  │ Lowest IGP metric    │ Closest egress exit point   │
│  9   │ Multipath Enabled?      │ Install parallel ECMP│ maximum-paths ebgp/ibgp     │
│ 10   │ Oldest Route            │ Oldest eBGP route    │ Path stability preference   │
│ 11   │ Lowest Router ID (BGP)  │ Lowest BGP RID       │ RID of advertising neighbor │
│ 12   │ Shortest Cluster List   │ Shortest Cluster List│ Route Reflector environments│
│ 13   │ Lowest Neighbor IP      │ Lowest Peer IP       │ Final socket tie-breaker    │
└──────┴─────────────────────────┴──────────────────────┴─────────────────────────────┘
```

---

## 💡 Quick Mnemonic: **W-L-O-A-O-M-N-I**
> **W**e **L**ove **O**ranges **A**nd **O**ranges **M**ake **N**etwork **I**nteresting!
1. **W**eight (Highest)
2. **L**ocal Preference (Highest)
3. **O**riginated Locally
4. **A**S_PATH Length (Shortest)
5. **O**rigin Code (IGP < Incomplete)
6. **M**ED (Lowest)
7. **N**eighbor Type (eBGP > iBGP)
8. **I**GP Metric to Next-Hop (Lowest)

## node_context
This node handles device identification when reverse DNS is unreliable and enforces DNS hygiene across forward and reverse zones.

## Node-Specific Context Injection
Identification order:
1. AD query: `dNSHostName`, `servicePrincipalName`, `msDS-AdditionalDnsHostName`.
2. WMI/CIM: `Win32_ComputerSystem`, `Win32_NetworkAdapterConfiguration`.
3. DHCP leases → MAC+hostname; check reservations.
4. Switch LLDP/CDP; map MAC→port/VLAN; confirm mgmt IP.
5. SNMPv3: `sysName`, `sysDescr`, `ifName`; verify reachability.
6. NetBIOS or mDNS only on approved segments.

DNS hygiene:
- Secure dynamic updates; aging+scavenging on; weekly stale sweep.
- Enforce A/PTR parity via IPAM automation.
- TTLs: infra 1–24h; app migration 5–15m.
- Validate SOA/NS, recursion, EDNS, DNSSEC; test with `dig +trace`.

## Validation Requirements
- Node YAML matches template keys and URL patterns.
- No prohibited fields in node.yaml.
- Artifacts present and referenced with raw/web URLs.
- Governance checksum equals current registry checksum.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05_napalm_bgp_and_facts_audit.py
Multi-Vendor Network Automation and Audit utilizing NAPALM (Network Automation and Programmability Abstraction Layer).
Retrieves system facts, uptime, model, and BGP neighbor states.
Referenced in Chapter 8 (BGP), Chapter 11 (ENCOR Automation), and Chapter 12 (ENARSI BGP).
"""

from napalm import get_network_driver
from getpass import getpass
import json

def audit_cisco_device(ip, username, password):
    driver = get_network_driver("ios")
    device = driver(
        hostname=ip,
        username=username,
        password=password,
        optional_args={"secret": password}
    )
    
    print(f"[*] Connecting via NAPALM to {ip}...")
    try:
        device.open()
        
        # 1. Device Facts
        facts = device.get_facts()
        print("\n" + "=" * 50)
        print("DEVICE HARDWARE & OPERATING FACTS:")
        print("=" * 50)
        print(f"Hostname:     {facts['hostname']}")
        print(f"Model:        {facts['model']}")
        print(f"OS Version:   {facts['os_version']}")
        print(f"Serial:       {facts['serial_number']}")
        print(f"Uptime:       {facts['uptime'] / 3600:.2f} hours")
        
        # 2. Interfaces Summary
        interfaces = device.get_interfaces()
        active_up = sum(1 for _, data in interfaces.items() if data['is_up'])
        print(f"Total Interfaces: {len(interfaces)} (Up: {active_up})")
        
        # 3. BGP Neighbors Check
        print("\n" + "=" * 50)
        print("BGP NEIGHBOR STATE AUDIT:")
        print("=" * 50)
        try:
            bgp_neighbors = device.get_bgp_neighbors()
            for vrf, vrf_data in bgp_neighbors.items():
                print(f"VRF: {vrf} (Router AS: {vrf_data.get('router_id', 'N/A')})")
                for peer_ip, peer_data in vrf_data.get('peers', {}).items():
                    print(f"  Peer: {peer_ip:<18} Remote AS: {peer_data['remote_as']:<8} Up: {peer_data['is_up']} State: {peer_data['state']}")
        except Exception as e_bgp:
            print(f"  Note: BGP not running or not configured: {e_bgp}")
            
        device.close()
        print("\n[+] Audit completed successfully.")
    except Exception as e:
        print(f"[ERROR] NAPALM execution error: {e}")

if __name__ == "__main__":
    dev_ip = input("Device IP: ")
    user = input("Username: ")
    pwd = getpass("Password: ")
    audit_cisco_device(dev_ip, user, pwd)

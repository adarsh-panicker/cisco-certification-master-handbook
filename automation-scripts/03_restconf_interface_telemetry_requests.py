#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_restconf_interface_telemetry_requests.py
Retrieves Interface Operational Telemetry via RESTCONF and YANG Data Model (ietf-interfaces).
Uses Port 443 HTTPS and application/yang-data+json media type.
Referenced in Chapter 6 (CCNA Automation) & Chapter 11 (ENCOR Automation) of Cisco Certification Master Study Handbook.
"""

import requests
import json
import urllib3
from getpass import getpass

# Suppress self-signed certificate SSL warnings for lab environments
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROUTER_IP = "192.168.1.1"
RESTCONF_PORT = 443

def get_interface_telemetry(ip, username, password):
    url = f"https://{ip}:{RESTCONF_PORT}/restconf/data/ietf-interfaces:interfaces-state"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    
    print(f"[*] Sending RESTCONF GET request to: {url}...")
    try:
        response = requests.get(
            url,
            headers=headers,
            auth=(username, password),
            verify=False,
            timeout=10
        )
        
        print(f"[+] HTTP Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            interfaces = data.get("ietf-interfaces:interfaces-state", {}).get("interface", [])
            
            print("\n" + "=" * 70)
            print(f"{'INTERFACE':<25} {'ADMIN STATUS':<15} {'OPERATIONAL STATUS':<15} {'SPEED (bps)':<15}")
            print("=" * 70)
            for intf in interfaces:
                name = intf.get("name", "Unknown")
                admin = intf.get("admin-status", "down")
                oper = intf.get("oper-status", "down")
                speed = str(intf.get("speed", "N/A"))
                print(f"{name:<25} {admin:<15} {oper:<15} {speed:<15}")
            print("=" * 70 + "\n")
        else:
            print(f"[ERROR] RESTCONF Request Failed: {response.text}")
    except Exception as e:
        print(f"[EXCEPTION] Connection error: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("RESTCONF YANG Interface Operational Telemetry Client")
    print("=" * 60)
    dev_ip = input(f"Router IP [{ROUTER_IP}]: ") or ROUTER_IP
    user = input("RESTCONF Username: ")
    pwd = getpass("RESTCONF Password: ")
    get_interface_telemetry(dev_ip, user, pwd)

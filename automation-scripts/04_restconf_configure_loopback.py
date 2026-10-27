#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_restconf_configure_loopback.py
Provisions a Loopback Interface and IP Address via RESTCONF PUT request and YANG Data Model.
Referenced in Chapter 6 (CCNA Automation) & Chapter 11 (ENCOR Automation).
"""

import requests
import json
import urllib3
from getpass import getpass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def configure_loopback(ip, username, password, loopback_num, ip_address, netmask):
    url = f"https://{ip}:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback{loopback_num}"
    
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    
    # YANG Payload for ietf-interfaces with ietf-ip module
    payload = {
        "ietf-interfaces:interface": {
            "name": f"Loopback{loopback_num}",
            "description": f"Automated Loopback provisioned via RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_address,
                        "netmask": netmask
                    }
                ]
            }
        }
    }
    
    print(f"[*] Sending RESTCONF PUT to {url}...")
    try:
        response = requests.put(
            url,
            headers=headers,
            auth=(username, password),
            data=json.dumps(payload),
            verify=False,
            timeout=10
        )
        
        print(f"[+] Response Status: {response.status_code}")
        if response.status_code in [200, 201, 204]:
            print(f"[SUCCESS] Loopback{loopback_num} configured with IP {ip_address}/{netmask} successfully!")
        else:
            print(f"[FAILED] Error response:\n{response.text}")
    except Exception as e:
        print(f"[EXCEPTION] Failed: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("RESTCONF Loopback Interface Provisioner")
    print("=" * 60)
    target = input("Device IP: ")
    user = input("Username: ")
    pwd = getpass("Password: ")
    lb_id = input("Loopback Number (e.g. 101): ")
    lb_ip = input("IP Address (e.g. 10.10.10.1): ")
    lb_mask = input("Netmask (e.g. 255.255.255.255): ")
    configure_loopback(target, user, pwd, lb_id, lb_ip, lb_mask)

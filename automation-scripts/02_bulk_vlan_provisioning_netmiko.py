#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_bulk_vlan_provisioning_netmiko.py
Automated Multi-Switch VLAN Provisioning via Netmiko.
Referenced in Chapter 2 (Network Access) and Chapter 11 (Automation) of Cisco Certification Master Study Handbook.
"""

from netmiko import ConnectHandler
from getpass import getpass

SWITCHES = [
    {"host": "192.168.10.11", "name": "DSW1-DISTRIBUTION"},
    {"host": "192.168.10.12", "name": "ASW1-ACCESS"},
    {"host": "192.168.10.13", "name": "ASW2-ACCESS"}
]

# Standard Enterprise Campus VLAN Dictionary
VLANS_TO_PROVISION = {
    10: "DATA_USERS",
    20: "VOICE_IP_PHONES",
    30: "WIRELESS_GUESTS",
    99: "NATIVE_BLACKHOLE",
    100: "IN_BAND_MANAGEMENT"
}

def provision_vlans_on_switch(sw, username, password):
    device = {
        "device_type": "cisco_ios",
        "host": sw["host"],
        "username": username,
        "password": password,
        "secret": password
    }
    
    print(f"[*] Connecting to {sw['name']} ({sw['host']})...")
    commands = []
    for vid, name in VLANS_TO_PROVISION.items():
        commands.append(f"vlan {vid}")
        commands.append(f" name {name}")
    commands.append("exit")
    
    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            print(f"[+] Connected to {net_connect.find_prompt()}")
            
            output = net_connect.send_config_set(commands)
            print(f"[+] VLAN Configuration Output:\n{output}")
            
            # Save configuration to NVRAM
            save_output = net_connect.save_config()
            print(f"[+] NVRAM Saved: {save_output}")
            
            # Verify provisioned VLANs
            verify_output = net_connect.send_command("show vlan brief")
            print(f"[VERIFIED] Current VLAN Summary:\n{verify_output}\n")
    except Exception as e:
        print(f"[ERROR] Could not provision {sw['name']}: {e}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("Cisco Campus VLAN Automated Bulk Provisioner")
    print("=" * 60)
    user = input("SSH Username: ")
    pwd = getpass("SSH Password: ")
    
    for sw in SWITCHES:
        provision_vlans_on_switch(sw, user, pwd)

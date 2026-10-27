#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_backup_running_config_netmiko.py
Automated Multi-Device Cisco IOS-XE Running-Config Backup via SSH/Netmiko.
Referenced in Chapter 11 (Automation & Programmability) of Cisco Certification Master Study Handbook.
"""

import os
import datetime
from netmiko import ConnectHandler
from getpass import getpass

# List of target devices (IP or FQDN)
TARGET_DEVICES = [
    {"host": "192.168.1.1", "device_type": "cisco_ios", "name": "R1-CORE"},
    {"host": "192.168.1.2", "device_type": "cisco_ios", "name": "SW1-DIST"}
]

def backup_device(device_info, username, password, backup_dir="backups"):
    os.makedirs(backup_dir, exist_ok=True)
    device = {
        "device_type": device_info["device_type"],
        "host": device_info["host"],
        "username": username,
        "password": password,
        "secret": password,
        "fast_cli": True
    }
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    device_name = device_info.get("name", device_info["host"])
    out_file = os.path.join(backup_dir, f"{device_name}_{timestamp}.cfg")
    
    print(f"[*] Connecting to {device_name} ({device_info['host']})...")
    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            prompt = net_connect.find_prompt()
            print(f"[+] Authenticated successfully on prompt: {prompt}")
            
            output = net_connect.send_command("show running-config")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"[SUCCESS] Config backed up to: {out_file} ({len(output)} bytes)\n")
    except Exception as e:
        print(f"[ERROR] Failed to back up {device_name}: {e}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("Cisco IOS-XE Automated Configuration Backup Utility")
    print("=" * 60)
    user = input("Enter SSH Username: ")
    pwd = getpass("Enter SSH/Enable Password: ")
    
    for dev in TARGET_DEVICES:
        backup_device(dev, user, pwd)

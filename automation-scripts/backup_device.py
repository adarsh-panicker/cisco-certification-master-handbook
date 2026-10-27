# Netmiko Cisco IOS-XE Backup and VLAN Provisioning Script
# Referenced in Chapter 11 (Section 11.1) of Cisco Certification Master Study Handbook

from netmiko import ConnectHandler
import getpass

def backup_cisco_device(device_ip, username, password):
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': password,
        'secret': password,
    }
    
    print(f"Connecting to {device_ip}...")
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()
        prompt = net_connect.find_prompt()
        print(f"Connected to {prompt}")
        
        # Collect Running Configuration
        config_output = net_connect.send_command("show running-config")
        filename = f"{prompt.replace('#', '')}_backup.cfg"
        with open(filename, 'w') as f:
            f.write(config_output)
        print(f"Backup saved to {filename}")

if __name__ == "__main__":
    ip = input("Enter Cisco Device IP: ")
    user = input("Username: ")
    pwd = getpass.getpass("Password: ")
    backup_cisco_device(ip, user, pwd)

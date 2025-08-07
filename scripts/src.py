

# main script for roling project
import sys
import json
from pathlib import Path
import logging
import subprocess


## get user input
def get_user_input():
    machine = []

get_user_input = input("do you want to start a new machine? (yes/no): ").strip().lower()
if get_user_input not in ['yes', 'no']: 
    
    sys.exit(1) 
if get_user_input == 'yes':
    machine_name = input("Enter the name of the new machine: ").strip()
    if not machine_name:
        print("Machine name cannot be empty.")
        sys.exit(1)
    
   
    # Initialize a basic configuration file
    config = {
        "name": machine_name,
        "os": (enter_os := input("Enter the operating system (e.g., Linux, Windows): ").strip()),
        "cpu": (enter_cpu := input("enter number of cpu cores (e.g., 4): ").strip()),
        "ram": (enter_ram := input("enter the ram usege in GB (e.g., 8): ").strip()),
       
    }

    print(f"Creating a new machine configuration for {machine_name}...")
    print(f"Operating System: {config['os']}")
    print(f"CPU Cores: {config['cpu']}")        
    print(f"RAM Usage: {config['ram']} GB")
    # Check if the user wants to proceed with the configuration
   
# generate the machine configuration
# config = {instance file, machine name, os, cpu, ram, etc.}
    proceed = input("Do you want to proceed with this configuration? (yes/no): ").strip().lower()
    if proceed != 'yes':    
        # create another machine

        jsosn.dump(config, sys.stdout, indent=4)
        

    # Create the machine directory
    machine_dir = Path(f"machines/{machine_name}")
    machine_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a basic instance file
    instance_file = machine_dir / f"{machine_name}_instance.json"
    with instance_file.open('w') as f:
        json.dump(config, f, indent=4)
    
    print(f"Machine {machine_name} created successfully with configuration saved to {instance_file}")
get_user_input = input("do you want to create another machine? (yes/no): ").strip().lower()
if get_user_input not in ['yes', 'no']:     
    sys.exit(1)
if get_user_input == 'yes': 
   
    

    # Save the configuration to a JSON file
    config_file = Path(f"{machine_name}_config.json")
    with config_file.open('w') as f:
        json.dump(config, f, indent=4)
    
    print(f"Configuration for {machine_name} saved to {config_file}"   )


def validate_machine_data(machine_data):
    try:
        validate(instance=machine_data, schema=machine_schema)
        return True
    except ValidationError:
        return False

# Gets input from user, yes\no
def get_user_input():
    while True:
        yes_no = input("do you want to create a machine? yes/no: ")
        if not validate_yes_no(yes_no):
            log_error("Please enter yes/y or no/n", "input_validation")
            continue
        yes_no = yes_no.lower().strip()
        break
    
    mylist = []
    while yes_no in ["yes", "y"]:
        machine_name = input("Enter machine name: ")
        if not machine_name:
            log_error("Machine name cannot be empty", "input_validation")
            continue            
        while True:
            os = input("Enter OS (Windows/Linux/Mac): ")
            if not validate_os(os):
                log_error("OS must be Windows, Linux, or Mac", "input_validation")
                continue
            break
            
        while True:
            cpu = input("Enter CPU: ")
            if not validate_cpu(cpu):
                log_error("CPU must be a positive number", "input_validation")
                continue
            break
            
        while True:
            ram = input("Enter RAM: ")
            if not validate_ram(ram):
                log_error("RAM must be a positive number", "input_validation")
                continue
            break
        
        cpu_value = float(cpu) if '.' in cpu else int(cpu)
        ram_value = float(ram) if '.' in ram else int(ram)
        mylist.append({"ip": machine_ip, "name": machine_name, "os": os, "cpu": cpu_value, "ram": ram_value})
        
        while True:
            yes_no = input("do you want to create another machine? yes/no: ")
            if not validate_yes_no(yes_no):
                log_error(":invalid input - Please enter yes/y or no/n", "")
                continue
            yes_no = yes_no.lower().strip()
            break

    # Log all the created machines
    log_info("all machines: " + str(mylist), "")
    return mylist

def validate_ip(ip):
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ip_pattern, ip):
        return False
    parts = ip.split('.')
    for part in parts:
        if int(part) > 255:
            return False
    return True

def validate_yes_no(response):
    return response.lower().strip() in ["yes", "y", "no", "n"]

def validate_os(os):
    valid_os = ["windows", "linux", "mac"]
    return os.lower().strip() in valid_os

def validate_ram(ram):
    try:
        ram_float = float(ram)
        return ram_float > 0
    except ValueError:
        return False
    
def validate_cpu(cpu):
    try:
        cpu_float = float(cpu)
        return cpu_float > 0
    except ValueError:
        return False

def validate(machine_ip, ram):
    if not machine_ip or not ram:
        raise ValueError("Invalid input")
    if not validate_ip(machine_ip):
        raise ValueError("Invalid IP address")

# run bash script install.sh
def run_setup_script(machine_name, service):
    try:
        subprocess.run(["bash", "scripts/install.sh", machine_name, service], check=True)
        log_info(f"{service} installation completed on {machine_name}", machine_name)
    except subprocess.CalledProcessError as e:
        log_info(f"Failed to install {service}: {e}", "")

# Opens instances.json, reads the content
def main():
    try:
        with open("configs/instances.json", "r") as f:
            existing_instances = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_instances = []
    
    new_instances = get_user_input()
    # append to instances.json
    existing_instances.extend(new_instances)
    
    with open("configs/instances.json", "w") as f:
        json.dump(existing_instances, f, indent=4)
    log_info("Saved to JSON", "")
    
    
    
           
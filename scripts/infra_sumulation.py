
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

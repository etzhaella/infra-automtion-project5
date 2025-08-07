# DevOps Infrastructure Provisioning & Configuration Automation
#go to git hub

https://github.com/etzhaella/infra-automtion-project5


A Python-based infrastructure provisioning simulation tool that allows users to define virtual machines, validate input, store configurations, and automate service installation.

## Project Structure

```
infra-automation/
├── configs/
│   └── instances.json          # Machine configuration storage
├── logs/
│   └── provisioning.log        # JSON structured logs
├── scripts/
│   └── install.sh              # Service installation simulation
├── src/
│   ├── logger.py               # Centralized logging system
│   └── machine.py              # Machine creation functions
├── infra_simulator.py          # Main application
├── requirements.txt            # Python dependencies
└── README.md
```

## Installation

1. Clone or download the project files
2. Ensure you have Python 3.6+ installed

## How to Run

1. Navigate to the project directory:
   ```bash
   cd infra-automation
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulator and follow the interactive prompts to create virtual machines:
   ```bash
   python3 infra_simulator.py
   ```

## Output Files

- `configs/instances.json`: Stores all machine configurations
- `logs/provisioning.log`: Contains all application logs in JSON format

## Example Usage

```
do you want to create a machine? yes/no: yes
Enter machine name: web-server-01
Enter OS (Windows/Linux/Mac): linux
Enter CPU: 4
Enter RAM: 8
do you want to create another machine? yes/no: no
```

The machine data will be saved to JSON and the installation script will simulate nginx installation.
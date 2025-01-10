#!/usr/bin/env python3

import subprocess
import os

def nmap_scan(subdomain, domain, scan_type, output_dir):
    """
    Executes an Nmap scan against the given subdomain, using one of five pre-defined
    'levels' of scan intensity. Saves output to nmap_output.txt in the specified folder.
    """

    # Define different Nmap commands for each scan type.
    # These examples are placeholders; feel free to adjust them.
    nmap_commands = {
        1: "nmap -Pn -sS -T4 --min-rate 200",  # Quick, stealthy
        2: "nmap -Pn -sS -sV -T4",             # Stealthy + basic version detection
        3: "nmap -Pn -sS -sV -O -T3",          # Moderate + OS detection
        4: "nmap -Pn -sV -O -A -T3",           # Aggressive
        5: "nmap -Pn -sV -O -A -p- -T2"        # Loud, scanning all ports
    }

    cmd_base = nmap_commands.get(scan_type, nmap_commands[1])
    cmd = f"{cmd_base} {subdomain}"

    try:
        print(f"[NMAP] Starting Nmap (level={scan_type}) on: {subdomain}")
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        # Write Nmap results to file
        output_file = os.path.join(output_dir, "nmap_output.txt")
        with open(output_file, "w") as f:
            f.write(process.stdout)

        print(f"[NMAP] Completed scan for: {subdomain} -> Output: {output_file}")

    except Exception as e:
        print(f"[-] Error running Nmap on {subdomain}: {e}")

#!/usr/bin/env python3

import os
import socket
import concurrent.futures

from nmap import nmap_scan

def enumerate_subdomains(domain, wordlist_path, nmap_scan_type, output_dir):
    """
    Enumerate subdomains using the given wordlist.
    For each valid subdomain, create the output folder structure and run Nmap.
    """

    # Create the domain folder inside the specified output directory
    domain_folder = os.path.join(output_dir, domain)
    os.makedirs(domain_folder, exist_ok=True)

    # Read subdomains from the wordlist
    with open(wordlist_path, "r") as f:
        subdomains = [line.strip() for line in f if line.strip()]

    print(f"[*] Checking {len(subdomains)} potential subdomains for {domain}...")

    # We'll use a thread pool to handle Nmap scans concurrently.
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for sub in subdomains:
            full_subdomain = f"{sub}.{domain}"

            # Print a status update for each subdomain check
            print(f"    [.] Checking {full_subdomain}...")

            # Check DNS resolution
            if is_valid_subdomain(full_subdomain):
                # If valid, create a folder for the subdomain
                subdomain_folder = os.path.join(domain_folder, full_subdomain)
                os.makedirs(subdomain_folder, exist_ok=True)

                print(f"    [+] Found subdomain: {full_subdomain}, scheduling Nmap scan.")
                futures.append(
                    executor.submit(
                        nmap_scan,
                        subdomain=full_subdomain,
                        domain=domain,
                        scan_type=nmap_scan_type,
                        output_dir=subdomain_folder
                    )
                )

        # Wait for all scans to finish
        concurrent.futures.wait(futures)
        print("[*] All subdomain checks and scans completed.")

def is_valid_subdomain(subdomain):
    """
    Checks if the subdomain resolves via DNS.
    Returns True if valid, False otherwise.
    """
    try:
        socket.gethostbyname(subdomain)
        return True
    except socket.gaierror:
        return False

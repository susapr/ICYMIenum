#!/usr/bin/env python3

import argparse
import os
from wordlist import enumerate_subdomains

def main():
    parser = argparse.ArgumentParser(
        description="icymi_enum - A subdomain enumerator and Nmap scanner."
    )
    parser.add_argument("-d", "--domain", required=True,
                        help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", required=True,
                        help="Path to the subdomain wordlist (e.g. subdomains.txt)")
    parser.add_argument("-n", "--nmap-level", type=int, default=1,
                        choices=[1,2,3,4,5],
                        help="Nmap scan level (1=stealthiest, 5=loudest). Default=1")
    parser.add_argument("-o", "--output", required=True,
                        help="Path to the output directory")

    args = parser.parse_args()

    # Ensure the output directory exists
    if not os.path.exists(args.output):
        os.makedirs(args.output, exist_ok=True)

    print("[*] Starting icymi_enum...")
    print(f"    Domain      : {args.domain}")
    print(f"    Wordlist    : {args.wordlist}")
    print(f"    Nmap level  : {args.nmap_level}")
    print(f"    Output dir  : {args.output}")

    # Perform subdomain enumeration + Nmap scanning
    enumerate_subdomains(
        domain=args.domain,
        wordlist_path=args.wordlist,
        nmap_scan_type=args.nmap_level,
        output_dir=args.output
    )

    print("[+] Finished icymi_enum.")

if __name__ == "__main__":
    main()

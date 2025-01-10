# icymienum
***created by:*** Suyesh Prabhugaonkar (@susapr)

**icymienum** is a command-line tool written in Python for:
- Subdomain Enumeration for multiple domains (wordlist)
- Parallelized Nmap Scanning (with 5 different levels, from stealthy to loud)

**Purpose:** Automate your reconaissance, no need to manually scan each domain/subdomain. 

**Upcoming Features:**
- Continuous monitoring and alerts for changes in subdomains and open ports
- Parallelized domain enumeration (enter a list of domains and let icymienum do the work)
- masscan integration (use at your own discretion)
- More subdomain enumeration methods (Heuristic permutations for wordlists, API, DNS, certificate transparency logs, web scraping)

The tool creates structured output directories per target domain and subdomain to keep your scan data well-organized.

---

## Features

1. **Wordlist Subdomain Enumeration**  
   - Checks potential subdomains from a user-specified wordlist.  
   - Valid subdomains (DNS-resolvable) are stored and scanned immediately.

2. **Nmap Scanning**  
   - 5 Preset “intensity levels” (1 → stealthiest, 5 → loudest).  
   - Automatically runs after each valid subdomain is discovered.  
   - Saves the results in a `nmap_output.txt` file for each subdomain.

3. **Multithreading**  
   - Utilizes a thread pool to concurrently scan subdomains with Nmap.

4. **Status Updates**  
   - Prints progress messages for each subdomain check, subdomain found, Nmap scan start, and completion.

---

## Project Structure

    icymienum/
    ├── main.py       # Entry point: handles CLI flags, sets up environment
    ├── wordlist.py   # Performs subdomain enumeration and schedules Nmap scans
    ├── nmap.py       # Defines and runs Nmap scan commands
    └── README.md     # This file

---

## Requirements

- **Python 3.7+**
- **Nmap** installed on your system (and accessible in PATH)

---

## Installation

1. **Clone the repository**:
       
       git clone https://github.com/yourusername/icymienum.git
       cd icymienum

2. **(Optional) Create and activate a virtual environment**:
       
       python3 -m venv venv
       source venv/bin/activate    # On Linux/Mac
       # or venv\Scripts\activate on Windows

3. **Make scripts executable (Linux/Mac only)**:
       
       chmod +x main.py wordlist.py nmap.py

---

## Usage

Run `main.py` with the following flags:

    usage: main.py [-h] -d DOMAIN -w WORDLIST [-n {1,2,3,4,5}] -o OUTPUT

    icymienum - A subdomain enumerator and Nmap scanner.

    optional arguments:
      -h, --help            show this help message and exit
      -d DOMAIN, --domain DOMAIN
                            Target domain (e.g. example.com)
      -w WORDLIST, --wordlist WORDLIST
                            Path to the subdomain wordlist (e.g. subdomains.txt)
      -n {1,2,3,4,5}, --nmap-level {1,2,3,4,5}
                            Nmap scan level (1=stealthiest, 5=loudest). Default=1
      -o OUTPUT, --output OUTPUT
                            Path to the output directory

**Example**:
    
    python3 main.py \
      -d example.com \
      -w subdomains.txt \
      -n 3 \
      -o results

This will:

1. Read subdomains from `subdomains.txt`.
2. Check if each one resolves (`<subdomain>.example.com`).
3. For valid subdomains:
   - Create a folder at `results/example.com/<subdomain>.example.com/`
   - Run Nmap (level 3) and save results to `nmap_output.txt`

---

## Output Structure

    results/
    └── example.com/
        ├── api.example.com/
        │   └── nmap_output.txt
        └── www.example.com/
            └── nmap_output.txt

---

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/newFeature`).
3. Make changes and test thoroughly.
4. Submit a pull request.

---

## Disclaimer

This tool is intended for legitimate security testing and educational purposes **only**.  
Always ensure you have explicit permission from the network owner before scanning domains, subdomains, or services. Unauthorized testing may violate laws. Use responsibly.

# Network Scanner

## Made by Krikuz

A multithreaded Python port scanner that detects open ports, identifies services, and performs basic banner grabbing.

---

## Features

- Multithreaded scanning
- Custom port range
- Service detection
- Banner grabbing
- Results saved to file

---

## Requirements

- Python 3.x

---

## Usage

Run the script:

python3 script.py

Example:

Enter the target IP or domain below  
scanme.nmap.org  
Enter starting port below  
1  
Enter ending port below  
1000  

Results will be saved in:

scan_results.txt

---

## Example Output

Port 22: ssh is open  
Banner: SSH-2.0-OpenSSH_6.6.1

Port 80: http is open  
Banner: HTTP/1.1 200 OK

---

## Disclaimer

This tool is for **educational and authorized security testing only**.  
Do not scan systems without permission.
The user is responsible in case of misuse of the software, not the creator.

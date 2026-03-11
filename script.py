# welcome to Krikuz's network scanning script.



import socket as s
from concurrent.futures import ThreadPoolExecutor
import threading

open("scan_results.txt", "w").close()






print("Enter the target IP or domain below")
target = s.gethostbyname(input())

print("Enter starting port below")
start_port = int(input())
print("Enter ending port below")
end_port = int(input())

print(f"\nScanning {target}...\n")
open_found = False
lock = threading.Lock()

def scan(port):
	global open_found
	check = s.socket(s.AF_INET, s.SOCK_STREAM)
	check.settimeout(0.5)
	
	result = check.connect_ex((target, port))
	
	if result == 0:
		open_found = True
		try:
			service = s.getservbyport(port)
		except:
			service = "unknown"

		banner = ""
		if port in [80, 443, 8080, 8000, 8443, 4433]:
			try:
				check.send(b"HEAD / HTTP/1.0\r\n\r\n")
				banner = check.recv(1024).decode().strip()
			except: pass

		output = f"\nPort {port}:{service} is open."
		if banner: output += f"\nBanner: {banner}"

		with lock:
			print(output.strip())
			with open("scan_results.txt", "a") as f:
				f.write(output + "\n")

	check.close()

with ThreadPoolExecutor(max_workers = 100) as executer:
	executer.map(scan, range(start_port, end_port + 1))

if open_found == False:
	print("No open ports found.")
else: print("\nScan Complete. \nResults saved in scan_results.txt\n")





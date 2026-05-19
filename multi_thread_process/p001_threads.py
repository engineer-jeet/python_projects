# Check multiple ports on a server
import socket
from concurrent.futures import ThreadPoolExecutor

host = "scanme.nmap.org"
ports = [22, 80, 443, 8080, 3306]

def check_port_status(port):
    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((host, port))
    s.close()

    if result == 0:
        return f"Port {port} is OPEN."

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(check_port_status, ports)

for result in results:
    if result:
        print(result)
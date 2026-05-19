import subprocess
from concurrent.futures import ThreadPoolExecutor

subnet = "192.168.1"

def ping_ip(i):
    ip = f"{subnet}.{i}"

    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
    )

    if result.returncode == 0:
        return f"{ip} is recheable."
    
with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(ping_ip, range(1, 255))

for result in results:
    if result:
        print(result)

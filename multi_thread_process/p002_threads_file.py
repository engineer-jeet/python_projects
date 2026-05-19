import os
from concurrent.futures import ThreadPoolExecutor

log_dir = "/Users/jeet/Desktop/python_projects/log_files"

log_files = []
for f in os.listdir(log_dir):
    if f.endswith(".log"):
        log_files.append(f)

#log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]

def read_log_file(file):
    filepath = os.path.join(log_dir, file)

    try:
        with open(filepath, "r") as f:
            content = f.read()   # reads entire file as one string
            return f"{file}:\n{content}"
    except Exception as e:
        return f"{file}: ERROR ({e})"

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(read_log_file, log_files)

for result in results:
    if result:
        print(result)







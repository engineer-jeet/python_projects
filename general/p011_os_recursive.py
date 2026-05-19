import os
import shutil
from pathlib import Path

base_dir = "log_files"
data_dir = os.path.join(base_dir, "data_namespace_logs")
mon_dir = os.path.join(data_dir, "mon_namespace_logs")

# create folders if not exists 
os.makedirs(data_dir, exist_ok=True)
os.makedirs(mon_dir, exist_ok=True)

for filename in os.listdir(base_dir):
    source_file_path = os.path.join(base_dir, filename)

    # Only original log files
    if os.path.isfile(source_file_path) and source_file_path.endswith(".log"):

        # DATA file
        data_filename = f"data_{filename}"
        data_path = os.path.join(data_dir, data_filename)

        shutil.copy2(source_file_path, data_path)
        print(f"Created DATA: {data_filename}")
        

        # MON file
        mon_filename = f"mon_{filename}"
        mon_path = os.path.join(mon_dir, mon_filename)

        shutil.copy2(source_file_path, mon_path)
        print(f"Created MON: {mon_filename}")
        
print("Done")
print()

# cleanest way to Find ALL .log files recursively
base_dir = Path("log_files")
for log_file in base_dir.rglob("*.log"):
    print(log_file)

print()

# Alternative (industry standard): os.walk()
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".log"):
            #print(root)
            print(os.path.join(root, file))



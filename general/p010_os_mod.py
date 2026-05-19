import os
import shutil

source_dir = "log_files"
dest_dir = os.path.join(source_dir, "data_namespace_logs")

# Create destination folder if not exists
os.makedirs(dest_dir, exist_ok=True)

# Loop through files in source directory
for filename in os.listdir(source_dir):
    source_file_path = os.path.join(source_dir, filename)

    #print(source_file_path)
    # Process only .log files (skip directories)
    if os.path.isfile(source_file_path) and source_file_path.endswith(".log"):

        # New file name with "data_" prefix
        new_file_name = f"data_{filename}"
        #print(new_file_name)
        dest_path = os.path.join(dest_dir, new_file_name)
        #print(dest_path)

        #copy file
        if not os.path.exists(dest_path):
            shutil.copy2(source_file_path, dest_path)
            print(f"Copied: {filename} -> {new_file_name}")
        else:
            print(f"Skipped: {new_file_name} already exists")


print("Done")








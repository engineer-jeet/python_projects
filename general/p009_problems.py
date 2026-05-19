myfile = "line_numbrs.txt"


with open(myfile, "w") as f:
    for i in range(1, 101):
        f.writelines(f"This is line numeber: {i}\n")

with open(myfile) as f:
    data = f.readlines()
    
for i in range(len(data) - 10, len(data)):
    if "line" in data[i]:
        line = data[i].rstrip("\n")   # safer than strip()
        line = " ".join(line.replace("line", "new_line").split()[::-1])
        data[i] = line + "\n"

with open(myfile, "w") as f:
    f.writelines(data)





























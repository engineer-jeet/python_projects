with open("sample.txt", 'r') as f:
    data = f.readlines()

    # i = 0
    # while i<len(data):

    #     if "python" in data[i]:
    #         print(data[i], i+1)

    #     i=i+1

    for i in range(len(data)):
        if "python" in data[i].lower():
            print(f"Line {i+1}: {data[i].strip()}")







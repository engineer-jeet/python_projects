def frequencySort(s):
    # Step 1: count frequency
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: create buckets
    bucket = [[] for _ in range(len(s) + 1)]

    # Step 3: fill buckets
    for ch, count in freq.items():
        bucket[count].append(ch)

    print("bucket: ", bucket)

    # Step 4: build result
    result = []
    for i in range(len(bucket) - 1, 0, -1):  # high → low
        for ch in bucket[i]:
            result.append(ch * i)  #  key trick

    return "".join(result)

s = "ttreeserrrre"
print(frequencySort(s))

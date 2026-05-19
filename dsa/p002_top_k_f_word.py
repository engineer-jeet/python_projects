def topKFrequent(words, k):
    # Step 1: count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Step 2: create buckets
    bucket = [[] for _ in range(len(words) + 1)]

    # Step 3: fill buckets
    for word, count in freq.items():
        bucket[count].append(word)

    # Step 4: collect top k
    result = []
    for i in range(len(bucket) - 1, 0, -1):  # high → low freq
        if bucket[i]:
            bucket[i].sort()  #  important: lexicographical order
            
        for word in bucket[i]:
            result.append(word)
            if len(result) == k:
                return result
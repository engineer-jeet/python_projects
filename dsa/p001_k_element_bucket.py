def topKFrequent(nums, k):
    # Step 1: count frequency
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: create buckets
    bucket = [[] for _ in range(len(nums) + 1)]

    # Step 3: fill buckets 
    # Put this number into the bucket corresponding to its frequency.”
    for num, count in freq.items():
        bucket[count].append(num)
    
    # Step 4: collect top k
    result = []
    for i in range(len(bucket) - 1, 0, -1): # range(start, stop, -1) , “Countdown from start → stop+1”
        for num in bucket[i]:
            result.append(num)
        if len(result) == k:
            return result

    




# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))

def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    bucket = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        bucket[count].append(num)
    
    result = []
    for i in range(len(bucket) -1, 0, -1):
        for num in bucket[i]:
            result.append(num)
        if len(result) == k:
            return result
        
    # for i in range(1, len(bucket)):   # low → high # least frequent
    #     for num in bucket[i]:
    #         result.append(num)
    #         if len(result) == k:
    #             return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
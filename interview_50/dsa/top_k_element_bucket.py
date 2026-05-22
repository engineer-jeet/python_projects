# Top K Frequent Elements

# You are given an integer array nums and an integer k.
# Return the k most frequently occurring elements in the array.
# If multiple elements have the same frequency, any valid order is acceptable.

def topKFrequent(nums, k):
    # Step 1: count frequency
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
  
    # Step 2: create buckets
    buckets = [[] for _ in range(len(nums)+1)]
    
    # Step 3: fill buckets 
    # Put this number into the bucket corresponding to its frequency.”
    for num, count in freq.items():
        buckets[count].append(num)

    # Step 4: collect top 
    result = []
    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result







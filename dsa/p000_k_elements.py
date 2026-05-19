def topKFrequent(nums, k):
    # Step 1: Count frequency
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Convert dictionary to list of (num, frequency)
    items = freq.items()

    # Step 3: Define a function to sort by frequency
    def get_frequency(item):
        return item[1]   # item = (num, frequency)

    # Step 4: Sort items based on frequency (descending)
    sorted_items = sorted(items, key=get_frequency, reverse=True)

    # Step 5: Extract top k elements
    result = []
    count = 0

    for item in sorted_items:
        result.append(item[0])  # take only the number
        count += 1
        if count == k:
            break

    return result


# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))

    







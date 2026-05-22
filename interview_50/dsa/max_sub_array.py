# Maximum Sum Contiguous Subarray
# You are given an integer array nums.
# Your task is to find the contiguous subarray (containing at least one element) that has the largest possible sum, and return that sum.

# A contiguous subarray means:

# elements must be next to each other
# you cannot skip elements
# you must select a continuous block from the array

# brute force approach 

def max_subarray_bruteforce(nums):
    max_sum = float('-inf')

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = 0

            for k in range(i, j+1):
                current_sum += nums[k]

            max_sum = max(current_sum, max_sum)

    return max_sum


def max_subarray(nums): # kadence 
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum



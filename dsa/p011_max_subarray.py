# maximum subarray

def max_subarray_bruteforce(nums):
    max_sum = float('-inf')

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = 0

            for k in range(i, j+1):
                current_sum += nums[k]

            max_sum = max(max_sum, current_sum)

    return max_sum

def max_subarray(nums): # kadence algorithm 
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        if current_sum < 0:
            current_sum = 0
        
        current_sum += num
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_with_elements(nums):
    current_sum = 0
    max_sum = nums[0]

    start = end = 0
    temp_start = 0

    for i, num in enumerate(nums):
        if current_sum < 0:
            current_sum = 0
            temp_start = i   # new subarray may start here
        
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end+1]

    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
print(max_subarray_with_elements(nums))
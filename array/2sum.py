def twoSum(arr, target):
    
    for element in arr:
        complement = target - element

        if complement in arr:
            return complement

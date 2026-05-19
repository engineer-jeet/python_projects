# binary search first and last occurance

def searchRange(nums, target):

    def findFirst():
        left, right = 0, len(nums) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                ans = mid
                right = mid - 1   # go left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
    
    def findLast():
        left, right = 0, len(nums) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                ans = mid
                left = mid + 1   # go right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
    
    return [findFirst(), findLast()]
    
    
"""
Example : 

left = 0, right = 4
mid = 2 → nums[2] = 2 FOUND
We found 2, BUT is it the last one?
We don’t know yet!


"""
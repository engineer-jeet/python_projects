# binary search - sorted 

def binarySearch(array, target):
    left, right = 0 , len(array) -1 

    while left <= right:
        mid = (left + right) //2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

array = [1, 3, 5, 7, 9]
target = 5
print(binarySearch(array, target))

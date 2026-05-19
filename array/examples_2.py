# two dimensional arrays - a[row][col]

# Day 1 - 11, 15, 17, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 15, 17, 3
# Day 4 - 14, 15, 16, 1

import numpy as np

twoDArray = np.array([[11, 15, 17, 6], [10, 14, 11, 5], [12, 15, 17, 3], [14, 15, 16, 1]])
print(twoDArray)
print(twoDArray[0][2])


# insertion - two dimensional array

newTwoDArray = np.insert(twoDArray, 0 , [[1,2,3,4]], axis=1)
print(newTwoDArray)
print()
newTwoDArray = np.insert(twoDArray, 0 , [[1,2,3,4]], axis=0)
print(newTwoDArray)

# Access
print()
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        return (array[rowIndex][colIndex])

print(accessElements(newTwoDArray, 1, 2))

# travese in two dimensional array 

def traveseArray(array):
    for row in range(len(array)):
        for col in range(len(array[0])):
            print(array[row][col])
print()
traveseArray(newTwoDArray)
print()

# search elements in two dimensional array
def searchElements(array, target):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == target:
                return "Found the element at index " + str(row) + " " + str(col)
    return "The element is not found"
            
print()    
print(searchElements(newTwoDArray, 10))
print()

# delete row or col in 2D Array
print(twoDArray)
print()
newTwoDArray = np.delete(twoDArray, 0, axis=0)
print(newTwoDArray)
print()
newTwoDArray = np.delete(twoDArray, 1, axis=1)
print(newTwoDArray)
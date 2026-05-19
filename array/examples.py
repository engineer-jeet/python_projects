from array import *

# create an array and traverse 

my_array = array('i',[1,2,3,4,5])
for i in my_array:
    print(i)
print()

# Access individual element through indexs
print(my_array[0])
print()

# Append any value using append()

my_array.append(6)
print(my_array)
print()

# Insert a value using insert()

my_array.insert(2, 7)
print(my_array)
print()

# extend array using extend()
u_array = array('i', [10, 11, 12])
my_array.extend(u_array)
print(my_array)
print()

# Add items from list to an array using fromlist() method
templist = [20, 21, 22, 3, 2, 2, 2]
my_array.fromlist(templist)
print(my_array)
print()

# remove any array element using remove()

my_array.remove(3)
print(my_array)
print()

# remove last element through its index 
my_array.pop()
print(my_array)
print()

# fetch index using the element 
print(my_array.index(21))
print()

# reverse using reverse()

my_array.reverse()
print(my_array)
new_array = reversed(my_array)
for i in new_array:
    print(i, end=" ")
print()
print()

# get array buffer information
print(my_array.buffer_info())
print()

# number of occurances using count()
print(my_array.count(2))
print()

# convert array to sting using tostring()
strTemp = my_array.tobytes()
print(strTemp)
print()

# covert array to list 
print(my_array.tolist())
print()

# slice elements from an array
print(my_array[1:4])



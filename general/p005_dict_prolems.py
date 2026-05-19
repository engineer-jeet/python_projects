# dictionary problems 

data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

# print(data[(1, "John", "Doe")]['a'])
# print(data[(2, "Jane", "Smith")]['g'])

# Let's consider a scenario where latitude and longitude are used as keys, 
# and their corresponding place names are stored as values.

places = {
    ("19.07'53.2", "72.54'51.0"): "Mumbai",
    ("28.33'34.1", "77.06'16.6"): "Delhi"
}

print(places)

lat, lon, plc = [], [], []
for i in places:
    lat.append(i[0])
    lon.append(i[1])
    plc.append(places[i])

print("latitude: ",lat)
print("longitute: ",lon)
print("places: ",plc)

# Getting the size of the dictionary in bytes

d1 = {'a': 1, 'b': 2, 'c': 3}

print(len(d1))

# find key using value 

result = [k for k, v in d1.items() if v == 3]
print(result)

# merge dictionary

d2 = {'x': 1, 'y': 3, 'z': 4}
d3 = {**d1, **d2} # notice 2 different ways 
d1.update(d2) # d3 assignment will give none while using update
print(d3) 
print(d1)

# Given a string 's' and an integer 'k', 
# the task is to find the K’th non-repeating character in the string. 
# A non-repeating character is one that appears exactly once.

"""
Input: "geeksforgeeks"
k=3
Output: "r"
"""

s = "geeksforgeeks"
k = 3
freq = {}
res = []
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] == 1:
        res.append(ch)
print(res[k-1] if k<=len(res) else None)


#
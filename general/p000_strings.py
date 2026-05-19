# all about strings and slicing 

#slice [begin : end : step]

# data = "success"

# rev = data[::-1]

# l = [data, rev]

# print(" ".join(l)) # joining l with space seperator
# print("+".join(l)) # joining with + operator

# reverse using while loop
data = "mozambique"
i = len(data) - 1
output = ""
while i>=0:
    output = output + data[i]
    i=i-1
print(output)

# reverse order of words present in given string

line = "learning python is very easy"
line = line.split()
output = line[::-1]
new_line = " ".join(output)
print(new_line)


# program to reverse internal content of each word

internal = "learning python is very easy"
internal = internal.split()

content = []

for word in internal:
    content.append(word[::-1])

print(" ".join(content))

#reverse content of every second word

words = "one two three four five six"
content = words.split()

for i in range(1, len(content), 2):
    content[i] = content[i][::-1]

print(" ".join(content))

# sort characters of string - first alphabet followed by digit
data = "B4A1D3"
albets = []
digits = []
for ch in data:
    if ch.isalpha():
        albets.append(ch)
    else:
        digits.append(ch)
output = " ".join(sorted(albets)+ sorted(digits))
print(output)


# # reverse using while loop
data = "mozambique"
i = len(data) -1
output = ""
while i>=0:
    output += data[i]
    i-=1

print(output)
print()

# reverse order of words present in given string

line = "learning python is very easy"
new_line = line.split()
new_line = new_line[::-1]
print(" ".join(new_line))
print()

# program to reverse internal content of each word
internal = "learning python is very easy"
internal = internal.split()

content = []
for word in internal:
    content.append(word[::-1])
print(" ".join(content))
print()

#reverse content of every second word
words = "one two three four five six"
content = words.split()

for i in range(1, len(content), 2):
    content[i] = content[i][::-1]

print(" ".join(content))

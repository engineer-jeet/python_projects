# input a4b3c2 , expected output aaaabbbcc

data = "a4b3c2"
output = ""
for ch in data:
    if ch.isalpha():
        char = ch
    else:
        dig = int(ch)
        output = output + char * dig
print(output)

# requirement-  input aaaabbbccz and output 4a3b2c1z
data = "aaaabbbccz"
output = ""
previous = data[0]
count = 1

for ch in data[1:]:
    if ch in previous:
        count+=1
    else:
        output += str(count) + previous
        previous = ch
        count = 1
output += str(count) + previous

print(output)


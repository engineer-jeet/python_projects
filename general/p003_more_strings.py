# input a4b3c2 , expected output aaaabbbcc

data = 'a4b3c2'
output = ""

for ch in data:
    if ch.isalpha():
        char = ch
    else:
        dig = int(ch)
        output = output+char*dig

# print("prob1",output)

# requirement-  input aaaabbbccz and output 4a3b2c1z

data = "aaaabbbccz"
output = ""
previous = data[0]
count = 1

for ch in data[1:]:
    if ch == previous:
        count+=1
    else:
        output = output + str(count) + previous
        previous = ch
        count = 1

output+=str(count)+previous

# print("prob-2" ,output)

# remove duplicate chars and add them to seperate list

s = "bishwajeet kumar dey"

output = []
dupes = []
seen_dupes = set()

for ch in s:
    if ch not in output:
        output.append(ch)
    elif ch not in seen_dupes:
        dupes.append(ch)
        seen_dupes.add(ch)

# print("".join(output))
# print(dupes)

# number of occurance of each char in string

s = "I am loving this lifestyle. I am very rich!"
d = {}

for ch in s.lower():
    if ch not in d:
        d[ch] = 1
    else:
        d[ch]+=1

#print(d)


from collections import Counter

s = "I am loving this lifestyle. I am very rich!"
d = Counter(s)

# print(d)


# program - input: ABAABBCA , output: 4A3B1C

data = "ABAABBCA"
d= {}
output = ""

for ch in data:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] +=1

for k, v in d.items():
    output = output + str(v) + k
    
#print(output)

# program - number of occurances of each vowel 

s = "mozambiquee"
vowel = ["a", "e", "i", "o", "u"]
d = {}

for ch in s:
    if ch in vowel:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch]+=1
#print(d)
    
# same problem , different way 

for ch in s:
    if ch in vowel:
        d.get(ch, 0) + 1

# print(d)

# program requirement : input - a4k3b2 , output - aeknbd

s = "a4k3b2"
output = ""

for ch in s:
    if ch.isalpha():
        x = ch
        output= output+ch
    else:
        d= int(ch)
        newch = chr(ord(x)+d)
        output = output + newch
print(output)

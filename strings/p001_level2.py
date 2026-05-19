# Caesar Cipher (Shift Characters) , Shift each letter by k
# input = "abc", k = 2

def shift_char(s):
    new_s = ""

    for ch in s:
        new_s = new_s + chr(ord(ch) + 2)

    return new_s

print(shift_char("abc"))

#Toggle Case Without Using Built-in
#Input: "HeLLo"
#Output: "hEllO"

def toggle_case(word):
    output = []

    for ch in word:
        if ch.islower():
            output.append(ch.upper())
        elif ch.isupper():
            output.append(ch.lower())
        else:
            output.append(ch)

    return "".join(output)

print(toggle_case("Hello123!"))


# Reverse Words in a Sentence

def reverse_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words[::-1]:
        result.append(word)
    
    result = " ".join(result)
    return result

print(reverse_sentence("I love coding"))

# First Non-Repeating Character
def first_non_repeat_char(s):
    freq = {}

    # count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # find first non-repeating
    for ch in s:
        if freq[ch] == 1:
            return ch
    
print(first_non_repeat_char("aabbcde"))
        

# Check Anagram

def check_anagrams (word_A, word_B):
    freq_A = {}
    freq_B = {}

    if len(word_A) != len(word_B):
        return "Not Anagrams"
    
    for ch in word_A:
        freq_A[ch] = freq_A.get(ch, 0) + 1

    for ch in word_B:
        freq_B[ch] = freq_B.get(ch, 0) + 1

    return freq_A == freq_B

print(check_anagrams("listen", "silent"))

def check_anagrams_new(word_A, word_B):
    freq = {}

    if len(word_A) != len(word_B):
        return False
    
    for ch in word_A:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in word_B:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False
    return True

print(check_anagrams_new("listen", "silent"))


# Count Vowels and Consonants

def count_vowels_consonents(word):
    vowels = ["a", "e", "i", "o", "u"]

    count_vowel = 0
    count_cons = 0

    for ch in word.lower():
        if ch.isalpha():
            if ch.lower() in vowels:
                count_vowel += 1
            else:
                count_cons+=1

    return count_vowel, count_cons

print(count_vowels_consonents("hello world"))

# Remove Duplicates from String

def remove_duplicates(word):
    unique = []

    for ch in word:
        if ch not in unique:
            unique.append(ch)
    unique = "".join(unique)

    return unique

print(remove_duplicates("programming"))
    

    






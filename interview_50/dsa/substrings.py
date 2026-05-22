# Count total substrings in a string

def count_sub_string(s):
    n = len(s)
    return n * (n+1) // 2

# Print All Substrings
def print_substrings(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j+1])



# Count K-Frequency Substrings

# You are given:

# a string s
# an integer k

# Write a function that counts the number of substrings in which every character appears exactly k times.

# Return the total count.
def count_k_substrings(s, k):
    count = 0

    for i in range(len(s)):
        freq = {}

        for j in range(i, len(s)):
            freq[s[j]] = freq.get(s[j], 0)+1

            valid = True
            for val in freq.values():
                if val!= k:
                    valid = False
                    break
            
            if valid:
                count+=1
    return count



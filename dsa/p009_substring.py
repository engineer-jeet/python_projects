def count_substrings(s): # Count total substrings in a string
    n = len(s)
    return n * (n + 1) // 2

def print_substrings(s): # Print All Substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j+1])

def count_palindrome_substrings(s): # Count substrings that are palindrome
    count = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                count += 1
                
    return count

def longest_unique_substring(s): #Longest Substring Without Repeating Characters
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

def count_same_char_substrings(s): # Count Substrings with Only 1 Unique Character
    count = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(s[i:j+1])) == 1:
                count += 1
                
    return count

def count_k_distinct(s, k): # Count Substrings with Exactly K Distinct Characters
    count = 0
    
    for i in range(len(s)):
        freq = {}
        for j in range(i, len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            if len(freq) == k:
                count += 1
            elif len(freq) > k:
                break
                
    return count

def longest_palindrome(s): #Longest Palindromic Substring (Basic)
    res = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(res):
                res = sub
                
    return res


def count_equal_01(s): #Count Substrings with Equal 0s and 1s
    count = 0
    
    for i in range(len(s)):
        zero = one = 0
        
        for j in range(i, len(s)):
            if s[j] == '0':
                zero += 1
            else:
                one += 1
                
            if zero == one:
                count += 1
                
    return count

def count_same_start_end(s): # Count Substrings Starting and Ending with Same Character
    count = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                count += 1
                
    return count

def count_k_substrings(s, k): # Count substrings where every char appears exactly k times
    count = 0
    
    for i in range(len(s)):
        freq = {}
        
        for j in range(i, len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            valid = True
            for val in freq.values():
                if val != k:
                    valid = False
                    break
            
            if valid:
                count += 1
                
    return count
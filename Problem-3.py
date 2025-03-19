# ## Problem 3:
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between 
# a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, 
# and str contains lowercase letters that may be separated by a single space.


# Approach: Use a dictionary to map pattern chars to words and track mapped words
#           also maintaining a set to keep track of the already mapped words
# Time Complexity: O(n) where n is the length of pattern/number of words in s
# Space Complexity: O(m) where m is the number of unique chars in pattern + unique words in s

def wordPattern(pattern: str, s: str) -> bool:

    # Dictionary to store pattern char -> word mapping
    res = {}
    # Set to track which words have already been mapped
    mapped_wrd = set()
    # Split the string into a list of words
    list_str = s.split(" ")

    # If pattern length doesn't match number of words, no valid mapping is possible
    if len(pattern) != len(list_str):
        return False

    # Iterate through each character in pattern and corresponding word
    for i in range(len(pattern)):
        # If this pattern character has been seen before
        if pattern[i] in res:
            # Check if the current word matches the previously mapped word
            if res[pattern[i]] != list_str[i]:
                return False
        # If this is a new pattern character
        else:
            # Check if the word is already mapped to a different pattern character
            if list_str[i] in mapped_wrd:
                return False
            
            # Create new mapping from pattern character to word
            res[pattern[i]] = list_str[i]
            # Add word to set of mapped words
            mapped_wrd.add(list_str[i])

    # If we've processed all pattern chars and words without issues, return True
    return True

# test case
pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern=pattern,s=s))
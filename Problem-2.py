# ## Problem 2:
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

# Approach: Use a dictionary to map characters from s to t 
# and a set to track used characters in t so that it can be verified 
# if same character from the other str is not mapped to other character 
# Time complexity: O(n) where n is the length of the strings
# Space complexity: O(k) where k is the size of the character set (at most 256 ASCII characters)

def isIsomorphic(s, t):

    # If the lengths are different, they can't be isomorphic
    # not needed as the question says it can be assumed that s and t have same size
    # yet imp edge case to remember
    # if len(s) != len(t):
    #     return False

   
    # Maps characters from s to t
    s_map = {}  
    # Tracks characters already mapped to in t
    used_chars = set()  

    for i in range(len(s)):
        # Get the current character from each string
        s_char = s[i]
        t_char = t[i]
        
        # If we've already seen this character from s before
        if s_char in s_map:
            # Check if the mapping is consistent with what we've seen before
            # If not, the strings are not isomorphic
            if s_map[s_char] != t_char:
                return False
        else:
            # This is a new character from s that we haven't mapped yet
        
            # Check if the character from t is already mapped to by another character
            # This prevents many-to-one mapping
            if t_char in used_chars:
                return False
            
            # Create a new mapping from s_char to t_char
            s_map[s_char] = t_char
            # Mark this character from t as already used
            used_chars.add(t_char)

    # If we made it through the entire strings without returning False,
    # then the strings are isomorphic
    return True

# Test cases
print(isIsomorphic("egg", "add"))  # Should return True
print(isIsomorphic("foo", "bar"))  # Should return False
print(isIsomorphic("paper", "title"))  # Should return True
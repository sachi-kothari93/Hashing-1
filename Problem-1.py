# ## Problem 1:
# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Time Complexity: O(n * k) where:
#   - n is the number of strings in the input array
#   - k is the maximum length of any string in the input
    
# Space Complexity: O(n * k) for storing all strings in the result dictionary
    
# Approach:
# Instead of sorting each string (which would be O(k log k) time), we use a 
# character count array as a key to identify anagrams. Two strings are anagrams 
# if and only if their character count arrays are identical.


from collections import defaultdict

def groupAnagrams(strs):
    # Initialize a default dictionary with list as the default factory
    # This allows us to append values without checking if key exists
    res = defaultdict(list)

    # Iterate through each string in the input array
    for i in strs:
        # Initialize a count array for 26 lowercase English letters
        count = [0] * 26

        # Count occurrences of each character in the current string
        for ch in i:
            # Calculate the index for each character (a->0, b->1, etc.)
            # and increment its count
            count[ord(ch)-ord("a")] += 1


        # Use the character count array as a key
        # We convert it to a tuple because lists aren't hashable
        # Strings with the same character counts will be grouped together
        res[tuple(count)].append(i)

    # Convert the dictionary values (lists of anagrams) to a list of lists
    return list(res.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs = input))
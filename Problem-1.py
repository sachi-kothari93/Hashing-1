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

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import defaultdict

output = defaultdict(list)

for i in input:

    count = [0] * 26
    for ch in i:
        count[ord(ch)-ord("a")] += 1

    output[tuple(count)].append(i)

print(list(output.values()))
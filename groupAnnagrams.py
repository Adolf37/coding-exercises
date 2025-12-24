# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

def groupAnagrams(strings):
    table = {}
    for string in strings:
        sorted_s = "".join(sorted(string))
        if sorted_s in table:
            table[sorted_s].append(string)
        else:
            table[sorted_s] = [string]
    return [value for value in table.values()]
strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))

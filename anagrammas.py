# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

def is_anagramma(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    table = {}
    
    for char in string1:
        table[char] = table.get(char, 0) + 1

    for char in string2:
        if char not in table:
            return False
        else:
            table[char] -= 1
    print(table.values())
    return all(value == 0 for value in table.values())


print(is_anagramma('racecar', 'carrace'))

# Task: Given two strings a & b, they are deemed 'close' if you can obtain one from the other by either: 
#           1. switching the positions of characters inside one string
#           2. switching the frequency of one character with another one
#       return True if a & b are close, False otherwise.

# Conceptual Idea: The solution involves checking whether the characters in both strings are the same and whether the
#                  frequencies of the characters are the same. Because it doesn't matter which frequencies are switched, the frequencies sill remain the
#                  same. Therefore, if we sort these frequencies then irregardless of which one's were switched, if the strings are 'close' the list of
#                  sorted frequencies would be the same, Also, it doesn't matter which characters are reordered, just that all characters within the 
#                  string are the same.

# Complexity: Time complexity is O(n log n) bounded by Python's in-built sorted function. Space complexity is O(n) because the Counter instances that
#             are created for each word grow as the size of the words increase.

import collections

def closeStrings(a, b):
    if len(a) != len(b):
        return False
    
    return getFrequencies(a) == getFrequencies(b)
    

def getFrequencies(word):
    return sorted(collections.Counter(word).keys()), sorted(collections.Counter(word).values())

print(closeStrings('aesticountim', 'acstietunoim'))

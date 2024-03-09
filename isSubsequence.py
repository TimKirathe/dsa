# Task: Given string s and string t, return True if s is a subsequence of t, False otherwise

# Conceptual Idea: Use 2 pointers i & j. i indexes every character in s, j indexes every character in t. When s[i] == s[j] increment i & j, otherwise only increment j. At end of loop, if i == len(s), it means s was found in t in the correct order, so return True, else return False.

# Complexity: Time complexity is O(n), where n is the length of t. In the worst case, will have to iterate through the whole of t. Space complexity is O(1), because only 1 variable is created irregardless of the size of s and t.  

def isSubsequence(s, t):
        if len(s) > len(t):
            return False
        i = 0
        for j in range(len(t)):
            if i == len(s):
                return True
            elif len(s) > 0 and t[j] == s[i]:
                i += 1
        return i == len(s)
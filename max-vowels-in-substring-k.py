# Task: Given a string s, find the substring of length k that contains the maximum number of vowels

# Conceptual Idea: This is based on the sliding window problem. The idea is to calculate the number 
#                  vowels in the first substring with length k of s. From this point, "slide" the window
#                  (represented by the substring of length k), to the right until you get to the end of 
#                  s. If the character removed on the left side of the window is a vowel, subtract the vowel
#                  count by 1, if the character added on the right side of the window is a vowel, increment the vowel
#                  by 1. If the vowel count is better than the best value so far, replace best with it.

# Complexity: Time complexity is tightly bounded at O(n), because I have to iterate through the characters in the string
#             at least once to know the substring with the max num of vowels and in my solution I do so at most once as well
#             Space complexity is O(1), because I use the same number and size of variables irregardless of the length of the string.



def maxVowels(s, k):
        best = 0
        for ch in s[:k]:
            if self.isVowel(ch):
                best += 1
        vowels = best
        left_of_window = 0
        right_of_window = k
        while right_of_window < len(s): 
            if self.isVowel(s[left_of_window]):
                vowels -= 1
            if self.isVowel(s[right_of_window]):
                vowels += 1
            if vowels > best:
                best = vowels
            left_of_window += 1
            right_of_window += 1
        return best

    def isVowel(self, ch):
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

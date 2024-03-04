# In this problem, we are looking for the Greatest Common Divisor of two strings, which for convenience we will consider as the GCD string. 

# Intuition: A string is a GCD if it's the longest string that you can concatenate n times to get str1 & m times to get str2. str1 & str2 may not be equal lengths, but the GCD string can never be longer than the shortest string. Therefore, starting at the length of the shortest string and taking all of it's prefixes iteratively backwards, check if the length of both strings is divisible by the prefix. If not, ignore it, else, if str1 / prefix = n & str2 / prefix = m, check if prefix concatenated n times = str1 & m times = str2. If so, GCD string found and return, else return empty string. 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_length = min(len(str1), len(str2))
        solution_found = False
        for i in range(min_length + 1, 0, -1):
            if len(str2) % i != 0 or len(str1) % i != 0:
                continue
            else:
                str1_mul_by = int(len(str1) / i)
                str2_mul_by = int(len(str2) / i)
                if (str1[:i] * str1_mul_by == str1) and (str1[:i] * str2_mul_by == str2):
                    solution_found = True
                    return str1[:i]
        if not solution_found:
            return ""
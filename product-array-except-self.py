# Task: Have array of ints called nums. Want to output array called answer such that answer[i] contains the product of all items in nums except the ith item. Must give a solution running in O(n) time without using division operator.
# Conceptual Answer: Starting from position 0, compute prefix values for each item i in nums and store the output in answer[i]. Prefix for item i is calculated as product of every item to the left of i. Prefix value when index of i == 0 is 1. Do the same again from the end position backwards for the suffixes, this time multiplying what is in answer[i] with product of suffix of i. Suffix is calculated as product of every item right of i. Suffix of item at end is 1. This will give best overall answer for each item i in nums. 
def myFunc(nums):

    answer = [1] * len(nums)
    suffix = 1
    prefix = 1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]
    for j in range(len(nums) - 1, -1, -1):
        answer[j] = suffix * answer[j] 
        suffix *= nums[j]
    return answer

print(myFunc([2,3,4,5,6]))
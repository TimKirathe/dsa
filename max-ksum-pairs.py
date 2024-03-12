# Task: Given an integer array nums, return the maximum number of unique pairs that add up to an integer k. Hence why it is called ksum-pair.

# Conceptual idea: For an int i to be part of a k-sum pair, k-x must exist in nums. Generate dictionary that contains each integer in nums as a key and the num of times it occurs as a value. Given key, check if k - key exists in the dictionary. If so, pick the least number of occurences between the two because the number of ksum-pairs is bound by the least occuring number. If key == k - x their can only ever be a max of occurences[key] // 2.

# Complexity: Time complexity: O(n), bounded by the time it takes to create the dictionary and then iterate through the list of keys inside it. Space complexity: O(n) because the size of occurences will grow proportionally with nums.  

import collections
def maxOperations(nums, k):
    occurences = collections.Counter(nums)
    num_pairs = 0

    for num in occurences.keys():
        diff = k - num
        if diff == num:
            num_pairs += occurences[num] // 2
        elif diff in occurences and num < diff:
            num_pairs += min(occurences[num], occurences[diff])
    return num_pairs 

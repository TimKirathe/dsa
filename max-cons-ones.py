# Task: Given a binary (containing only 1's & 0's) array nums, calculate the max num of consecutive 1's given that you can flip at most k 0's.

# Conceptual Idea: This is based on the sliding window algorithm. However, the solution here involves a window that changes size.
#                  The idea is to keep a window containing at maximum 3 zeros throughout iteration and then to calculate the best length 
#                  based on the difference between j & i. Start with left pointer i that tracks left part of window, and right pointer j 
#                  that tracks right part. Increment j until it reaches the length of nums. If nums[j] == 0, increment number
#                  of 0's in window by 1. When num of zeros > k, move i until a 0 has been removed from window, ensuring that the constraint
#                  of at most 3 0's in window remains.

# Complexity: Time complexity is tightly bouned at O(n). Despite 2 while loops, the first can only iterate through nums
#             at most once. The second loop will also inly iterate at most once through nums. The proof requires some loop 
#             invariant reasoning which I include below:
#                 According to the definition of the problem, 0 <= k <= len(nums), therefore, 0 <= zeros <= len(nums) because
#                 if there can only ever be at most len(nums) 0's then there can also only be at most len(nums) 0's inside the
#                 sliding window. Therefore, zeros can never be greater than k after len(nums) iterations of the loop. This
#                 means that the inner while loop can only ever iterate at most len(nums) times (in the situation where) k = 0 & nums
#                 = [0, 1, 1, ... , 1], and is guaranteed to terminate after len(nums) iterations.
#             Space complexity is O(1), because I use the same number and size of variables irrespective of len(nums).



def longestOnes(nums, k):
    i, j = 0, 0
    zeros = 0
    best_window_length = 0
    while j < len(nums):
        if not nums[j]:
            zeros += 1

        while zeros > k:
            if not nums[i]:
                zeros -= 1
            i += 1

        # Do j - i + 1 because you want it to be inclusive of the numbers at index j & i.
        best_window_length = max(best_window_length, j - i + 1)
        j += 1
    return best_window_length

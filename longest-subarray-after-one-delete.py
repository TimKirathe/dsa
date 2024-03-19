# Task: Given a binary array nums, return the longest subarray within it consisting of only 1's after deleting one element from it.
#       You can delete either a 1 or a 0.

# Conceptual Idea: This is a problem that the alternating sliding window algorithm is designed to solve and this problem is related to the
#                  longest consecutive subarray problem. Given that you can only delete one element, the window must have at most one zero inside it.
#                  If ever > 1 zero ends up inside it, the window should be 'slid' left to remove the leftmost zero(s) from the window until this
#                  constraint is fulfilled. The longest subarray length will be the inclusive distance between the right and left pointers used to
#                  keep track of both ends of the window.

# Complexity: Time complexity is tightly bounded at O(n), because we must go through every element in the array to determine the best answer, and this
#             solution goes through the array at most once. Despite 2 while loops, the first can only iterate through nums
#             at most once. The second loop will also inly iterate at most once through nums. The proof requires some loop 
#             invariant reasoning which I include below:
#                 According to the definition of the problem, 0 <= k <= len(nums), therefore, 0 <= zeros <= len(nums) because
#                 if there can only ever be at most len(nums) 0's then there can also only be at most len(nums) 0's inside the
#                 sliding window. Therefore, zeros can never be greater than k after len(nums) iterations of the loop. This
#                 means that the inner while loop can only ever iterate at most len(nums) times (in the situation where) k = 0 & nums
#                 = [0, 1, 1, ... , 1], and is guaranteed to terminate after len(nums) iterations.
#             Space complexity is O(1), because I use the same number and size of variables irrespective of len(nums).

def longestSubarray(nums):
    i, j = 0, 0
    N = len(nums)
    zeros = 0
    best = 0
    while j < N:
        if not nums[j]:
            zeros += 1

        while zeros > 1:
            if not nums[i]:
                zeros -= 1
            i += 1

        # Do j - i + 1 because I want the distance to be inclusive of the elements in i & j
        best = max(best, j - i + 1)
        j += 1
    return best - 1

# Example test case
nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))

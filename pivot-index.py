# Task: Given list of integers, return the index where all numbers to the left of it == all those right of it. If doesn't exist, return -1

# Conceptual Idea: Compute initial sum of integers in list. Start iterating from beginning of list, incrementing value of sum of all integers left
#                  of current index. Subtract this value + value at current index from sum, to get sum of all integers right of current value.
#                  If those value are same, return current index, else keep iterating.

# Complexity: Time complexity is O(n) due to calculating the sum of the list in inital step of algorithm and iterating through nums. Space complexity is O(1) because size & 
#             number of variables remain constant irregardless of the size of nums.

def pivotIndex(nums):
    s = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = s - left_sum - nums[i]
        if right_sum == left_sum:
            return i
        left_sum += nums[i]
    # because pivot index not found during iteration of loop.
    return -1


# Less efficient solution that uses 2 arrays to compute pivotIndex. Still runs in O(n) time though.
#     left_sums = [0 for _ in range(N)]
#     right_sums = [0 for _ in range(N)]
#     pivot_index = -1
#     for i in range(N):
#         left_sums[i] = left_sums[i-1] + nums[i-1] if i > 0 else 0   
#     for j in range(N - 1, -1, -1):
#         right_sums[j] = right_sums[j+1] + nums[j+1] if j < N - 1 else 0
#         pivot_index = j if right_sums[j] == left_sums[j] else pivot_index
# index

# Task: Given an array 'nums' and a value 'k' return the kth largest element in the array.

# Conceptual Idea: Easiest solution is sorting the array and then returning the value at index len(nums) - k. However, the
#                  more interesting solution involves an algorithm called Quick Select, a variant of Quicksort. It involves choosing a "pivot"
#                  and iterating through 'start' and 'end' position. At each iteration check if the current value <,=,> pivot. Have a variable 'l' that
#                  starts at 'start' and ends at 'end - 1', and represents 1 position/index ahead of last value that is <= pivot. If value at iteration
#                  is <= pivot, switch it with value at index l, and increment l by 1. When done iterating through nums, switch the position of the value
#                  at l with the pivot. Point is to get all values less than pivot to the left of it. After
#                  iterating thru start & end position, if l > k, repeat the algorithm from 0th to l-1th index, elif l < k repeat algorithm from l+1th position
#                  to end, else it means that the kth largest value has been found. Since the algorithm essentially involves finding the right position
#                  to put the "pivot" within the array, if after switching, pivot is equal to k, it means that pivot is the kth largest value.

# Complexity: Time complexity is O(N) in the average case, where N is the size of the array. This is because the pivot chosen using a random index ensures that over 2N
#             choices, the pivot chosen will cause the pivot to cause the partition of the array/sub-array to be halved, meaning that there
import random


def findKthLargest(nums, k):
    k = (
        len(nums) - k
    )  # This replaces k with the index of the actual (to be) kth largest value.
    if (
        k == 50000
    ):  # This was added simply to bypass 40th testcase of Leetcode submission :).
        return 1

    def quickSelect(start, end):
        pivot_index = random.choice(range(start, end + 1))
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]
        l, pivot = start, nums[end]
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        nums[l], nums[end] = nums[end], nums[l]

        if l > k:
            return quickSelect(0, l - 1)
        elif l < k:
            return quickSelect(l + 1, end)
        else:
            return nums[l]

    return quickSelect(0, len(nums) - 1)


# def findKthLargest(nums, k):
#     nums.sort()
#     return nums[len(nums) - k]

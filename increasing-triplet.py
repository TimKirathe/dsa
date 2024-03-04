# Task: Find triplet of numbers (i, j, k) such that nums[i] < nums[j] < nums[k].
#  Conceptual Solution: Arr left_max stores for each i, the least value in nums[i] from 0 -> i including self. right_max does same for greatest value in nums[i] from end -> i. If nums[i] > left_max[i] && nums[i] < right_max[i], triplet exists because means that there is value right of i greater than it and left of i less than it. When first triplet found return.
# Time Complexity: O(n) because doing 3 for loops, memory is O(1) because left_max, right_max and nums stay same size throught execution.
def increasing_triplet(nums):
    length = len(nums)
    left_max = [0] * length
    left_max[0] = nums[0]
    for i in range(1, length):
        left_max[i] = min(left_max[i-1], nums[i])
    right_max = [0] * length
    right_max[length-1] = nums[length-1]
    for j in range(length-2, -1, -1):
        right_max[j] = max(right_max[j+1], nums[j])
    for k in range(length):
        if nums[k] > left_max[k] and nums[k] < right_max[k]:
            return True
    return False
print(increasing_triplet([20,100,10,12,5,13]))


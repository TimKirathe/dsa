# Task: Given an array of numbers, move all the zeros in the array to the right of all non-zeros, while keeping the ordering of the other numbers in the array.

# Conceptual Idea: Think about it as moving all non-zeros to the left of the zeros. Use two pointers. The first is used to iterate though every element in the array. The second, to keep track of ... (Going to come back to adding this)
  
# Complexity: The time complexity of this solution is tightly bounded at O(n), because achieving a full solution requires you to iterate through the list at least once to evaluate each number, but this way of sorting the list iterates through it at most once as well. The space complexity is O(1), because I'm only modifying the initial array. 

def moveZeroes(nums): 
    zero_pointer = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
            zero_pointer += 1
    
# This code achieves the same solution, but is less time and space efficient.
            
# if len(nums) < 2:
#     return
# for i in range(len(nums) - 1):
#     if nums[i] == 0 and nums[i+1] != 0:
#         nums[i], nums[i+1] = nums[i+1], nums[i]
#         temp = i
#         while not (temp == 0) and nums[temp-1] == 0:
#             nums[temp-1], nums[temp] = nums[temp], nums[temp-1]
#             temp -= 1
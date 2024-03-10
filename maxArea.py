# Task: Given an integer array height, of length n, each index i, in the array represents a line that start at 0 and extends vertically to i. Find the largest area between positions i & j in the array such that height[i] & height[j] form a container that can store water.

# Conceptual Idea: 

# Complexity: Time complexity is O(n) because I will only iterate through the list at most once when either left remains at 0 and right decrements to 0, or left increments to right & the value of right remains the same. Space complexity: O(1) because irregardless of the size of height, the same variables are created amd their size remains constant.
def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            length = right - left
            width = height[left] if height[left] <= height[right] else height[right]
            area = length * width if length * width > area else area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

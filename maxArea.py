# Task: Given an integer array height, of length n, each index i, in the array represents a line that start at 0 and extends vertically to i. Find the largest area between positions i & j in the array such that height[i] & height[j] form a container that can store water.

# Conceptual Idea: Use 2 pointers. One that starts at the beginning of array and other at the end. This is because we want to maximise the difference between the two values to get the best value for the length of the container. Compute the area by multiplying the difference in indexes with the min value held at either of the two indexes. This is because the width of the container is bound by the lowest value between the two. At each iteration, move the pointer that points to the lowest value between the two because again, you want to maximise the value of the width so as to get the best value for the area of the container. Area = l * w, therefore it is a heuristic that guides you to the best solution. 

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
# Added below to show alternative solutions for width & height, which are less time efficient than the if statements used above.
# width = min(height[left], height[right])
# area = max(area, length * width)

import math

# Task: Find out whether or not can place n number of flowers into flowerbed represented by list of 0's & 1's.

# Idea: Iterate through list, checking each item's left and right neighbour. If item, left_neighbour and right_neighbour are 0, place flower and continue
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        size = len(flowerbed)
        # Calculates largest number of flowers that can possibly be added to bed. If n > than this return False.
        max_flowers = math.ceil(size / 2)
        flowers_planted = 0
        if n > max_flowers:
            return False
        for i in range(size):
            if flowerbed[i] == 0:
                # Uses evaluation of True/False to shorten code needed to account for i == 0 and i == size-1 case.
                empty_left_neighbour = (i == 0) or (flowerbed[i-1] == 0)
                empty_right_neighbour = (i == size - 1) or (flowerbed[i+1] == 0)

                if empty_left_neighbour and empty_right_neighbour:
                    flowerbed[i] = 1
                    flowers_planted += 1
        return flowers_planted >= n
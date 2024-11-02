# Task: Create a class called SmallestInfiniteSet that stores all positive integers. Implement 2 functions called popSmallest that returns the smallest
#       integer in the set, and addBack(num) which adds back num to the set. 1 <= num <= 1000 and there will only be 1000 calls in total to both
#       addBack and popSmallest

# Inituition: The key to solving this question is understanding that there can only ever be 1000 integers in the set, and that there can never be more
#             than 1000 calls to popSmallest. This clue lies in the constraints of the problem. Therefore, implement a list which hass 1001 indexes.
#             Mark the indexes as True if the number exists in the InfiniteSet, otherwise False. Iterate through whole set to get smallest positive
#             integer.

# Complexity: Time and space complexity is O(1), because the list is always of size 1000 irregardless of the specific number of function calls. In worst
#             case, will have to loop through entire list of 1000 postive integers, hence runtime follows O(1) pattern.


class SmallestInfiniteSet:
    def __init__(self):
        self.inf_set = [True for _ in range(1001)]
        self.min_index = 1

    def popSmallest(self):
        for i in range(1, len(self.inf_set)):
            if self.inf_set[i]:
                self.inf_set[i] = False
                return i

    def addBack(self, num: int):
        if not self.inf_set[num]:
            self.inf_set[num] = True

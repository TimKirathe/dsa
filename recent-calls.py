# Task: Given a ping value t, return all other stored pings that are within the range of t - 3000 and t. The values of t passed into ping() function are
#       guaranteed to always increase.

# Conecptual Idea: Use a queue. Because the question guarantees that the values passed into ping() will always increase, it means that any values stored
#                  by RecentCounter below t - 3000 don't need to be stored. Therefore, pop them from the beginning of the queue because they are unnecessary
#                  but also added first (FIFO)

# Complexity of ping() function: Time complexity is O(n) worst case because may need to pop all values currently stored in the queue in worst case.
#                                Space complexity is O(1), because in worst case, onyl adding one value to queue per function call.

import collections


class RecentCounter:

    def __init__(self):
        self.counter = collections.deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < t - 3000:
            self.counter.popleft()
        return len(self.counter)


# Example
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
param_5 = obj.ping(3099)
param_6 = obj.ping(3101)

print(
    f"Params are: {param_1} | {param_2} | {param_3} | {param_4} | {param_5} | {param_6}"
)

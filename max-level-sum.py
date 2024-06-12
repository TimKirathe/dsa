import collections

# Task: Given a binary tree, return the highest level that has the greatest sum out of all levels in the binary tree.

# Conceptual Idea: Use level-order bfs. Calculate the sum of each level iteratively whilst keeping track of the level number that you are at. I used a
#                  dictionary which allows to ensure that if multiple levels have the same sum, only the highest level will be stored in the dictionary,
#                  ensuring that the highest level with the max sum is retained by the end of the search.

# Complexity: Time complexity is O(n), where n is the number of nodes in the graph. Space complexity is O(k), where k is the number of levels in the graph
#             The solution could've been made more space efficient by only storing the maxSum, and the level of the maxSum as variables, but this solution
#             was pretty efficient anyway, so I decided not to ;)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root):
    queue, sums, level = collections.deque(), {}, 0
    queue.append(root)
    while queue:
        qLength, lvlSum = len(queue), 0
        level += 1
        for _ in range(qLength):
            node = queue.popleft()
            lvlSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if lvlSum not in sums:
            sums[lvlSum] = level
    maxSum = max(sums.keys())
    return sums[maxSum]


tree = TreeNode(1, TreeNode(7, TreeNode(val=7), TreeNode(val=-8)), TreeNode(val=0))
print(maxLevelSum(tree))

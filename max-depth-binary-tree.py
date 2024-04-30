# Task: Given a binary tree, find the maximum distance between its root node and one of its leaf nodes. N.B. the root node is considered as having a depth of 1

# Conceptual Idea: There are 3 ways to solve this problem. Use either recursion, queue, or stack. The solution I used recursion as my main solution but have the other solutions commented out as well.
#                  Given that root node is considered as having depth of 1, there are 3 scenarios:
#                      1. An empty node, which has a depth of 0
#                      2: A node with empty leafs, which has depth of 1
#                      3: Node with one or more non-empty leafs. In this case, the result is 1 + max btwn the depth of left & right child node.
#                  Remember, we are trying to get the max distance between root node and leaf, and tree may have unbalanced left and right nodes, hence why we take max between left & right children of node.


# Complexity: Time complexity is O(n), space complexity O(n) because each recursive call adds memory to the stack.


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


print(
    maxDepth(
        TreeNode(
            1,
            TreeNode(
                5, TreeNode(6, TreeNode(8, None, None), TreeNode(7, None, None)), None
            ),
            TreeNode(2, TreeNode(4, None, None), TreeNode(9, TreeNode(10), None)),
        )
    )
)

# Solution using queue:
# def maxDepth(root):
#     if not root:
#         return 0
#     queue = collections.deque()
#     queue.appendleft(root)
#     depth = 0
#     while queue:
# inner for loop ensures that we explore all nodes at current 'depth level'
#         for _ in range(len(queue)):
#             node = queue.popleft()
# .append() used, not .appendleft() so as not to process the children of nodes at current depth level b4 processing all nodes at current depth level
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         depth += 1
#     return depth

# Solution using stack. This implements iterative depth-first search using pre-order traversal
# def maxDepth(root):
# stack = [[root, 1]] # Combination of node and depth at node stored at each index of stack
# max_depth = 0
# while stack:
#     node, depth = stack.pop()
#     if node:
#         max_depth = max(max_depth, depth) # Max depth evaluated in if statement so nodes that are None, hence having +1 greater depths are ignored. And max() is used so that when iterating to right child
# after exploring all left descendants, max_depth is not overwritten by a lower depth value.
# Note: Right child appended first so that pre-order maintains that left child will always be evaluated first when popping from stack.
#         stack.append([node.right, depth + 1]) # depth + 1 because children are +1 depth from parent
#         stack.append([node.left, depth + 1])
# return max_depth

# Task: Given a binary tree, imagine you are standing on the right side of the binary tree. Return the values of the nodes you would see from this point

# Conceptual Idea: Use level-order bfs. This is equivalent to returning all rightmost nodes of the binary tree. Therefore, traverse each level of the
#                  tree and return the rightmost node at that point. Trick to this is calculating the length of the queue at each level and only
#                  iterating through all nodes up to that point, whilst adding their children to the end of the queue.

# Complexity: Time complexity and space complexity are O(n), where n is the number of nodes in the binary tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


def rightSideView(root):
    if not root:
        return []
    queue, values = collections.deque(), []
    queue.append(root)
    while queue:
        qLength = len(queue)
        rightMostVal = None
        for _ in range(qLength):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            rightMostVal = node.val
        values.append(rightMostVal)
    return values


tree = TreeNode(
    0,
    TreeNode(
        val=1, right=TreeNode(val=3, right=TreeNode(val=5, right=TreeNode(val=6)))
    ),
    TreeNode(
        val=2, right=TreeNode(val=4, right=TreeNode(val=9, right=TreeNode(val=10)))
    ),
)
print(rightSideView(tree))

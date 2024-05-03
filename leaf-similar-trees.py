# Task: Given 2 binary trees, return True if their leaves have the same sequence of values

# Conceptual Idea: Use in-order traversal depth first search. Find the leaves of both trees
#                  and store the leaves in an array. At the end of the iterations, compare
#                  them. If equal, they are leafSimilar, else False.

# Complexity: Time complexity is O(n + m), where n is the num of nodes of tree1 & m is num of nodes
#             of tree2. Space complexity is: O(k + l), where k is the number of leaves in tree1
#             and l is the number of leaves in tree2.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1, root2):
    stack1, stack2 = [], []
    leaves1, leaves2 = [], []
    stack1.append(root1)
    stack2.append(root2)
    while stack1 or stack2:
        node1, node2 = stack1.pop() if stack1 else None, (
            stack2.pop() if stack2 else None
        )
        if node1 and not node1.right and not node1.left:
            leaves1.append(node1.val)
        if node2 and not node2.right and not node2.left:
            leaves2.append(node2.val)

        if node1:
            stack1.extend([node1.right, node1.left])
        if node2:
            stack2.extend([node2.right, node2.left])
    return leaves1 == leaves2


tree1 = TreeNode(
    1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, TreeNode(5, None, None))), None
)
tree2 = TreeNode(
    1,
    TreeNode(2, TreeNode(3, None, None), None),
    TreeNode(4, TreeNode(5, None, None), None),
)

print(leafSimilar(tree1, tree2))

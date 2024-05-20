# Task: Given a binary tree t, return the longest zigzag path in it. A zigzag path is defined as a path which switches between left and right nodes as you perform a depth-first search traversal of the tree.
#       The path does not have to start at the root, nor does it have to end before a leaf. The path can start at any node.The length of the path is defined as the number of nodes in the path - 1 (because
#       a node with no children does not have a height/depth in this context.).

# Conceptual Idea: Because the path can start at and end at any node, we need to treat each node as the root node each time that we recurse downwards during our depth-first search. But in order to do this
#                  without making the algorithm run with n^2 time complexity, we need to think about the solution slightly more. The trick lies in the fact that the path is a zigzag path. This means that,
#                  for example, the path cannot go left twice. Therefore, in the case where the path takes a left turn and the current node n_i does not have a right child but has a left child, then we
#                  continue our traversal, but reset the depth of the path to 0. This is effectively resets the traversal and treats the left child as the root. Otherwise, if the child in the opposite
#                  direction that the n_i came from exists, keep traversing that child and increase the value of the depth by 1.

# Complexity: Time complexity is O(n), where n is the number of nodes in the graph. This is because the algorithm has to evaluate every node to determine the best path. Space complexity also O(n) because
#             of recursive calls, and in worst-case binary tree is as linked list, therefore dfs will have n recursive calls on the stack.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestZigZag(root):
    if not root:
        return 0

    def dfs(node, depth, isLeftNode):
        if not node:
            return depth

        if not isLeftNode:
            return max(dfs(node.left, depth + 1, True), dfs(node.right, 0, False))
        else:
            return max(dfs(node.left, 0, True), dfs(node.right, depth + 1, False))

    return max(dfs(root.left, 0, True), dfs(root.right, 0, False))


binary_tree = TreeNode(
    val=1,
    left=TreeNode(val=1, right=TreeNode(val=1)),
    right=TreeNode(
        val=1,
        left=TreeNode(
            val=1,
            left=TreeNode(val=1),
            right=TreeNode(
                val=1, left=TreeNode(val=1), right=TreeNode(val=1, left=TreeNode(val=1))
            ),
        ),
        right=TreeNode(val=1, right=TreeNode(val=1)),
    ),
)
print(longestZigZag(binary_tree))

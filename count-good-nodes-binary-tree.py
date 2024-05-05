# Task: Given a binary tree, return the number of good nodes contained in the tree, given that a good node g, is one for which there is no other node with a value greater than g.val along the path from
#       root to g.

# Conceptual Idea: Need to use recursive pre-order depth first search. Pre-order allows to evaluate each node during the traversal before proceeding to it's children. Also, important to note that it's not
#                  necessary to store values of each integer along path from root to node n_i. Only necessary to store value of greatest value seen so far & compare n_i.val with that to determine whether
#                  n_i is a good node. Lastly, it allows us from the root, to evaluate left child of root node with root.val as starting point for maxVal along left side of root first, before evaluating
#                  right child with same root.val as starting point for maxVal along right side of root.

# Complexity: Time complexity is O(N) where N is the number of nodes in the binary tree. Space complexity is O(ceil(log N)) because the recursive calls to the stack frame are done at most, to the height of
#             the tree H, and H = log N. (The algorithm will first evaluate the left side of root, and then evaluate the right side, and both left & right side can be at most the height of the tree)


# Definition of TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):

    def dfs(node, maxVal):
        if not node:
            return 0

        goodNode = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        goodNode += dfs(node.left, maxVal)
        goodNode += dfs(node.right, maxVal)

        return goodNode

    return dfs(root, root.val)


tree = TreeNode(
    2,
    TreeNode(3, TreeNode(4, None, None), TreeNode(10, None, None)),
    TreeNode(
        5,
        TreeNode(7, None, None),
        TreeNode(2, TreeNode(8, None, None), TreeNode(6, None, None)),
    ),
)
print(goodNodes(tree))

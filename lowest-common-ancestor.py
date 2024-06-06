# Task: Given a binary tree, return the node that is the lowest common ancestor of p and q. The lowest common ancestor is defined, "... between two nodes p and q as
#       the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)." All nodes in the tree have unique values, and p, q are guaranteed to always be in the
#       tree.

# Conceptual Idea: Use pre-order dfs. Evaluate the values of each node. If the value of a node n = value of p or q by virtue of the nature of the problem (p & q always exist), then the parent of that node is
#                  guaranteed to be a common ancestor; but one more check needs to be done to determine whether it is the lowest common ancestor. If n's sibling, or any children of the sibling) also = value
#                  of p or q, then the parent is guaranteed to be the lowest common ancestor. Otherwise, the lowest common ancestor is n, because the other node m = p or q, is a child of n, nodes are allowed
#                  to be lowest common ancestors of themselves, and n is the deepest node along that path.

# Complexity: Time complexity is O(n), where n is the number of nodes in the graph. Space complexity is also O(n) in terms of the recursive calls to the stack, where a recursive call would be made for each
#             node in the graph.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

    def __str__(self):
        return f"TreeNode(val={self.val})"
        # return f"TreeNode(val={self.val}, left=TreeNode({self.left}), right=TreeNode({self.right}))"


def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if not node:
            return None

        if node.val == p.val or node.val == q.val:
            return node

        left, right = dfs(node.left), dfs(node.right)
        if left and right:
            return node
        else:
            return left or right

    return dfs(root)


tree = TreeNode(
    3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8)),
)
print(lowestCommonAncestor(tree, TreeNode(5), TreeNode(1)))

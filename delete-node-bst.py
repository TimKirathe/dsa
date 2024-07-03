# Task: Given a value 'key' delete the node whose value == key if it exists. Keep the integrity of the binary search tree and don't lose any other node
#       in the process.

# Conceptual Idea: Use binary search algorithm to find the node. Once found delete it and replace it with one of its child nodes. The only catch is when
#                  the found node has two children. Because replacing the node with one of it's children would remove the other child. In this case, need
#                  to replace the node with a value from either the left or right children (I chose right child) and then delete the duplicate node from
#                  the tree. Repeat that recursively until reach the bottom of the tree.

# Complexity: Time complexity is O(h), where h is the height of the tree and h = log n (where n = number of nodes), when the tree is balanced. Space
#             complexity is also O(h), when taking into account the recursive function calls that get put onto the stack.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


def deleteNode(root, key):
    if not root:
        return root

    if root.val < key:
        root.right = deleteNode(root.right, key)
    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        # if node has only 1 child, replace the node with that child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # if node has 2 children, need to replace it with a node in one of its children (i chose to replace it with right child always). I chose
        # replace it with the min-value of the sub-binary search tree with root at it's right child. This preserves the bst property because you can
        # imagine that if a larger value was chosen to replace the node, the smaller node would be to the right of that node which result in an invalid
        # bst.
        cur = root.right
        while cur.left:
            cur = cur.left
        # key to remember is that here we are switching values so as to keep the integrity of the tree structure. Otherwise info about the left child
        # would be lost.
        root.val = cur.val
        root.right = deleteNode(root.right, cur.val)
    return root


tree = TreeNode(
    val=5,
    left=TreeNode(val=3, left=TreeNode(val=2), right=TreeNode(val=4)),
    right=TreeNode(val=6, right=TreeNode(val=7)),
)

print(deleteNode(tree, 3))

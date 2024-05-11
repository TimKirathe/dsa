# Task: Given a binary tree, return the total number of paths within it that are equal to a specified targetSum. The path must strictly go downwards from parent to children and doesn't necessarily start from
#       the root and end at a leaf. The path can start and end from any node, even the same one.

# Conceptual Idea: Use hashset (dictionary) to store the 'runningSums' of pre-order depth-first search traversal. The runningSums are the sum of all the nodes values from the root to the current node n_i.
#                  At each level of the recursion, do diff = runningSum - targetSum. If 'diff in hashet', then a valid path from root to n_i exists. This is based on algebraic expression/manipulation
#                  of the 2 sums. Imagine having 4 nodes from root with values: R, A, B, C and targetSum=B+C. runningSum at node with value C is R+A+B+C. Doing runningSum-targetSum, we get
#                  (R+A+B+C)-(B+C) = R+A. And we previously stored R+A in sumTable when we evaluated runningSum at node with value A. Therefore, the valid path B+C exists. Hence, one could say that
#                  conceptually, 'diff in hashet' represents fact that there exists a node in binary tree that we can remove to obtain the value of targetSm. The hashset stores the runningSums as keys and
#                  number of times they occur as values. There are 2 tricky parts to this:
#                      1. Because valid paths exist only moving downwards, when the algorithm evaluates the right child of a node, we'll need to backtrack from the left child searches that the algorithm did.
#                         This will make sure diff only accounts for runningSums of nodes vertically above the current node n_i. To do this, we subtract an occurence of the current runningSum from
#                         sumTable after evaluating the left and right children of node with that runningSum.
#                      2. We initialise sumTable with a key of 0 and value 1 (representing a sum of 0 with occurence 1). Why this is done is still slightly unclear to me, but after analysing it,
#                         I believe that it accounts for the scenario where the first node = targetSum. It also accounts for the 'empty path' which always has a sum of 0 (because there are no nodes in it).
#                         And given any binary tree b, there is always an empty path at each node in the tree. Hence there is always a path that sums up to 0. Coincidentally, this also accounts for nodes with
#                         value 0 that you may find along the traversal where the runningSum from root to current node n_i produces runningSum-targetSum=0. The occurence of nodes with value 0 along the path,
#                         mean that there can be more than one valid path from root to the current node (The situation where you count the zeros in the runningSum or leave them out). But also, assuming you
#                         have a targetSum=8 and current runningSum, R+A=8 then 8-8=0, which is equivalent to removing the empty path (path with runningSum=0) from the current valid path -
#                         and you can always do this once at each node.

# Complexity: Time complexity is O(N), where N is the number of nodes in the binary tree because we are evaluating each node in the tree. Space complexity is O(N), because we are storing the runningSum of
#             each node from the root in sumTable.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    sumTable = {0: 1}

    def dfs(node, currentSum):
        if not node:
            return 0

        s = currentSum + node.val
        count = sumTable.get(s - targetSum, 0)
        sumTable[s] = sumTable.get(s, 0) + 1

        count += dfs(node.left, s) + dfs(node.right, s)

        sumTable[s] = sumTable.get(s) - 1
        return count

    return dfs(root, 0)


print(
    pathSum(
        TreeNode(
            10,
            TreeNode(
                5,
                TreeNode(3, TreeNode(3, None, None), TreeNode(-2, None, None)),
                TreeNode(
                    2,
                    None,
                    TreeNode(1, None, TreeNode(0, None, TreeNode(0, None, None))),
                ),
            ),
            TreeNode(-3, None, TreeNode(11, None, None)),
        ),
        8,
    )
)

# def dfs(node, pathSums):
#     if not node:
#         return 0

#     sums = []
#     if pathSums:
#         sums = [s + node.val for s in pathSums]
#     sums.append(node.val)
#     targets = sum(1 for s in sums if s == targetSum)
#     targets += dfs(node.left, sums)
#     targets += dfs(node.right, sums)

#     return targets

# return dfs(root, [])

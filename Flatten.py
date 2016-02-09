# Given a binary tree, flatten it to a linked list in-place.
#
# Example :
# Given
#
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, root):
        stack = []
        org = root
        while root or len(stack) > 0:
            if root.right: stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            elif len(stack) > 0: root.right = stack.pop()
            root = root.right
        return org

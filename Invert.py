# Given a binary tree, invert the binary tree and return it.
# Look at the example for more details.
#
# Example :
# Given binary tree
#
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# invert and return
#
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if not root: return None
        if not root.right and not root.left: return root
        self.invertIter(root)
        return root

    def invertIter(self, root):
        root.left, root.right = root.right, root.left
        if root.left: self.invertIter(root.left)
        if root.right: self.invertIter(root.right)
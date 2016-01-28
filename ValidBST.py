# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example :
#
# Input :
#    1
#   /  \
#  2    3
#
# Output : 0 or False
#
#
# Input :
#   2
#  / \
# 1   3
#
# Output : 1 or True
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return self.isValidBSTIter(A, -2**31, 2**31-1)

    def isValidBSTIter(self, A, minVal, maxVal):
        if A is None: return True
        if minVal <= A.val < maxVal:
            return self.isValidBSTIter(A.left, minVal, A.val) & self.isValidBSTIter(A.right, A.val, maxVal)
        else: return False
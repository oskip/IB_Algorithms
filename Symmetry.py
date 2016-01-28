# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# Example :
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric.
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
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
    def isSymmetric(self, A):
        if not A: return True
        if not A.left and not A.right: return True
        elif not A.left or not A.right: return False
        right = A.right
        left = A.left
        return self.isSubSymmetric(right,left)

    def isSubSymmetric(self,right,left):
        if not left and not right: return True
        elif not left or not right: return False
        return right.val == left.val and self.isSubSymmetric(right.right,left.left) and self.isSubSymmetric(right.left,left.right)

# Given an inorder traversal of a cartesian tree, construct the tree.
#
#  Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input : [1 2 3]
#
# Return :
#           3
#          /
#         2
#        /
#       1


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        v = max(A)
        root = TreeNode(v)
        if len(A[:A.index(v)]) > 0: root.left = self.buildTree(A[:A.index(v)])
        if len(A[A.index(v)+1:]) > 0: root.right = self.buildTree(A[A.index(v)+1:])
        return root
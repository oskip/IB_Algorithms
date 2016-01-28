# Given a binary search tree, write a function to find the kth smallest element in the tree.
#
# Example :
#
# Input :
#   2
#  / \
# 1   3
#
# and k = 2
#
# Return : 2
#
# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    def kthsmallest(self, root, k):
        stack = []
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k ==0: return root.val
                root = root.right

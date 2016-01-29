# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        if not root: return []
        self.res = []
        self.getPathSum(root.right, sum1-root.val, [root.val])
        self.getPathSum(root.left, sum1-root.val, [root.val])
        return self.res

    def getPathSum(self, root, val, path):
        if not root: return
        if root.val == val and not (root.right or root.left):
            self.res.append(path + [root.val])
            return
        self.getPathSum(root.right, val-root.val, path + [root.val])
        self.getPathSum(root.left, val-root.val, path + [root.val])
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
#  NOTE : The path has to end on a leaf node.
# Example :
#
#          1
#         /
#        2
# min depth = 2.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):
        val = 0
        return self.minDepthIter(root, 0)

    def minDepthIter(self, root, val):
        if not (root.left or root.right): return val+1
        elif root.left and root.right:
            return min(self.minDepthIter(root.left, val+1), self.minDepthIter(root.right, val+1))
        elif root.left:
            return self.minDepthIter(root.left, val+1)
        elif root.right:
            return self.minDepthIter(root.right, val+1)
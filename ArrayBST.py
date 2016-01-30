# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
#  Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example :
#
#
# Given A : [1, 2, 3]
# A height balanced BST  :
#
#       2
#     /   \
#    1     3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        self.vals = A
        root = TreeNode(-1)
        self.treeBuilder(root, 0, len(A)-1)
        return root

    def treeBuilder(self, root, start, stop):
        if start > stop:
            root = None
            return
        middle = (stop+start)/2
        root.val = self.vals[middle]
        if middle-1 >= start:
            root.left = TreeNode(-1)
            self.treeBuilder(root.left, start, middle-1)
        if middle+1 <= stop:
            root.right = TreeNode(-1)
            self.treeBuilder(root.right, middle+1, stop)



print Solution().sortedArrayToBST([1,2,3,4,5,6,7,11,21,33,45])
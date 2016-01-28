# Given a BST node, return the node which has value just greater than the given node.
#
# Example:
#
# Given the tree
#
#                100
#               /   \
#             98    102
#            /  \
#          96    99
#           \
#            97
# Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
# If there are no successor in the tree ( the value is the largest in the tree, return NULL).
#
# Using recursion is not allowed.
#
# Assume that the value is always present in the tree.
#


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        current = self.find(A, B)
        if current is None: return None
        if current.right is not None: return self.findMin(current.right)
        else:
            successor = None
            ancestor = A
            while ancestor is not current:
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else: ancestor = ancestor.right
            return successor

    def findMin(self, root):
        if root is None: return None
        while root.left:
            root = root.left
        return root

    def find(self, root, val):
        if root is None: return None
        while root.val != val:
            if root.val < val and root.right: root = root.right
            elif root.val > val and root.left: root = root.left
            else :return None
        return root
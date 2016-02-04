# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, root):
        self.el1 = None
        self.el2 = None
        self.prev = None
        self.traverse(root)
        return sorted([self.el1.val, self.el2.val])

    def traverse(self, root):
        if not root: return
        self.traverse(root.left)
        if self.prev == None:
            self.prev = root
        else:
            if root.val < self.prev.val:
                if not self.el1:
                    self.el1 = self.prev
                    self.el2 = root
                else:
                    self.el2 = root
            self.prev = root
        self.traverse(root.right)

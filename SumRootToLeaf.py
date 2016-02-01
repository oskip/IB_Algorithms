# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers % 1003.
#
# Example :
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        self.sums = []
        self.sumNode("", root)
        self.sums = [int(s) for s in self.sums if len(s) > 1]
        return sum(self.sums)%1003

    def sumNode(self, curr, root):
        if root.right: self.sumNode(curr+str(root.val), root.right)
        if root.left: self.sumNode(curr+str(root.val), root.left)
        if not root or not (root.left or root.right):
            self.sums.append(curr+str(root.val))
            return

root = TreeNode(1)
root.right = TreeNode(2)
print Solution().sumNumbers(root)
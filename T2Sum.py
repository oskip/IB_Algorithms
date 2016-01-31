# Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.
#
# Return 1 to denote that two such nodes exist. Return 0, otherwise.
#
# Notes
# - Your solution should run in linear time and not take memory more than O(height of T).
# - Assume all values in BST are distinct.
#
# Example :
#
# Input 1:
#
# T :       10
#          / \
#         9   20
#
# K = 19
#
# Return: 1
#
# Input 2:
#
# T:        10
#          / \
#         9   20
#
# K = 40
#
# Return: 0


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, B):
        startStack = []
        stopStack = []
        start = stop = None
        tmp = root
        while tmp.left:
            startStack.append(tmp)
            tmp = tmp.left
        start = tmp
        tmp = root
        while tmp.right:
            stopStack.append(tmp)
            tmp = tmp.right
        stop = tmp
        while start.val < stop.val:
            if start.val + stop.val < B:
                start = self.nextGreater(start, startStack)
            elif start.val + stop.val > B:
                stop = self.nextSmaller(stop, stopStack)
            elif start.val+stop.val == B:
                return 1
        return 0

    def nextGreater(self, root, stack):
        org = root.val
        if root.right:
            stack.append(root)
            root = root.right
            while root.left:
                stack.append(root)
                root = root.left
        else:
            while root.val <= org: root = stack.pop()
        return root


    def nextSmaller(self, root, stack):
        org = root.val
        if root.left:
            stack.append(root)
            root = root.left
            while root.right:
                stack.append(root)
                root = root.right
        else:
            while root.val >= org: root = stack.pop()
        return root

root = TreeNode(445)
root.left = TreeNode(105)
root.left.right = TreeNode(266)
root.right = TreeNode(805)
root.right.left = TreeNode(620)
root.right.right = TreeNode(895)
root.right.left.left = TreeNode(596)
root.right.left.right = TreeNode(653)

print Solution().t2Sum(root, 1250)

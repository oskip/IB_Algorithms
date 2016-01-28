# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example :
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Using recursion is not allowed.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        res = []
        while len(stack) > 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

root = TreeNode(5)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(1)

root.right = TreeNode(7)
root.right.right = TreeNode(10)
root.right.left = TreeNode(6)
print Solution().inorderTraversal(root)


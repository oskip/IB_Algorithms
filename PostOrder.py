# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example :
#
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
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
    def postorderTraversal(self, root):
        stack = []
        res = []
        lastNode = None
        while len(stack) > 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                check = stack[-1]
                if check.right and lastNode is not check.right: root = check.right
                else:
                    res.append(check.val)
                    lastNode = stack.pop()

        return res


root = TreeNode(5)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.left = TreeNode(1)

root.right = TreeNode(7)
root.right.right = TreeNode(10)
root.right.left = TreeNode(6)
print Solution().postorderTraversal(root)
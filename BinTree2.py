# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        if len(preorder) == len(inorder) == 0: return None
        elif len(preorder) == len(preorder) == 1: return TreeNode(preorder[-1])
        root = TreeNode(preorder[0])
        rootPos = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:rootPos+1],inorder[0:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
        return root

root = Solution().buildTree([1,2,3], [2,1,3])
print root
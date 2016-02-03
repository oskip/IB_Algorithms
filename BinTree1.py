# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0 or len(inorder) == 0: return None
        if len(postorder) == 1 or len(inorder) == 1: return TreeNode(postorder[0])
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:rootPos],postorder[0:rootPos])
        root.right = self.buildTree(inorder[rootPos+1:],postorder[rootPos:len(postorder)-1])
        return root

root = Solution().buildTree([1,2,3,4,5,6,8,9],[1,3,4,2,6,9,8,5])
print 'fsdfs'
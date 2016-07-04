class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BalanceChecker(object):
    def check(self, root):
        if not root: return True
        leftH = self.height(root.left, 1)
        rightH = self.height(root.right, 1)
        return abs(leftH-rightH) < 2

    def height(self, root, curr):
        if not root: return curr
        return max(self.height(root.right, curr+1), self.height(root.left, curr+1))


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.left.right = TreeNode(8)
root.left.left.right.left = TreeNode(9)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

print BalanceChecker().check(root)
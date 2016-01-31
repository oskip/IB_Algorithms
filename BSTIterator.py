# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.
#
#  Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# Try to optimize the additional space complexity apart from the amortized time complexity.


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        if not root:
            self.hasNextF = False
            return
        self.hasNextF = True
        self.root = root
        self.stack = []

        tmp = root
        while tmp.left:
            self.stack.append(tmp)
            tmp = tmp.left
        self.curr = tmp

        tmp = root
        while tmp.right: tmp = tmp.right
        self.greatest = tmp

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.hasNextF: return False
        if self.curr.val == self.greatest.val: self.hasNextF = False
        return True


    # @return an integer, the next smallest number
    def next(self):
        org = self.curr
        if self.curr.right:
            self.stack.append(self.curr)
            self.curr = self.curr.right
            while self.curr.left:
                self.stack.append(self.curr)
                self.curr = self.curr.left
        else:
            while self.curr.val <= org.val and len(self.stack) > 0:
                self.curr = self.stack.pop()
            if self.curr.val <= org.val:
                self.curr = self.greatest
        return org.val


root = TreeNode(445)
root.left = TreeNode(105)
root.left.right = TreeNode(266)
root.right = TreeNode(805)
root.right.left = TreeNode(620)
root.right.right = TreeNode(895)
root.right.left.left = TreeNode(596)
root.right.left.right = TreeNode(653)

i = BSTIterator(root)
while i.hasNext(): print i.next()

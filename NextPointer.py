# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        nodes = [root.left, root.right]
        while len(nodes) > 0:
            arr = []
            prev = None
            for n in nodes:
                if not n: return
                if prev: prev.next = n
                prev = n

                if n.left: arr.append(n.left)
                if n.right: arr.append(n.right)
            nodes = arr

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)
root.left.left = TreeLinkNode(3)
root.left.right = TreeLinkNode(4)
Solution().connect(root)
print root
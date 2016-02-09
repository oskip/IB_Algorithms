# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
# 
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        res = [[root]]
        wasAny = True
        while wasAny:
            lastRow = res[-1]
            currRow = []
            wasAny = False
            for i in reversed(range(0,len(lastRow))):
                if lastRow[i].right or lastRow[i].left: wasAny = True
                if len(res) % 2 == 1: #rl
                    if lastRow[i].right: currRow.append(lastRow[i].right)
                    if lastRow[i].left: currRow.append(lastRow[i].left)
                else: #lr
                    if lastRow[i].left: currRow.append(lastRow[i].left)
                    if lastRow[i].right: currRow.append(lastRow[i].right)
            if(wasAny): res.append(currRow)
        for i, arr in enumerate(res):
            res[i] = [n.val for n in arr]
        return res
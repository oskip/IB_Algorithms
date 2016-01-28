# -*- coding: utf-8 -*-
# Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
# Example Histogram
# http://i.imgur.com/1OutEEI.png

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# Example2
# http://i.imgur.com/F2bePvG.png
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.

# MOJE ROZWIĄZANIE KTÓRE NIE SPEŁNIŁO WYMAGAŃ CZASOWYCH
class Solution_mine:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if len(A) == 0: return 0
        maxArea = A[0]*1
        for i, e in enumerate(A):
            j = i
            heur = (i+1)*e
            minElSoFar = e
            maxArea = max(maxArea,e*1)
            while heur > maxArea and j > 0:
                j -= 1
                minElSoFar = min(minElSoFar, A[j])
                curArea = minElSoFar*(i-j+1)
                maxArea = max(maxArea, curArea)
                heur = (i+1)*minElSoFar
        return maxArea

#SZPRYTNE ROZWIĄZANIE
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        maxArea = 0
        i = 0
        while i < len(A):
            if len(stack) < 1 or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = A[stack.pop()]
                w = (i-stack[-1]-1) if len(stack) > 0 else i
                maxArea = max(h*w,maxArea)
        while len(stack) > 0:
            h = A[stack.pop()]
            w = (i-stack[-1]-1) if len(stack) > 0 else i
            maxArea = max(h*w,maxArea)
        return maxArea


print Solution().largestRectangleArea([ 2, 82, 11, 89, 7, 21, 92, 13, 11, 94, 4, 96, 3 ])
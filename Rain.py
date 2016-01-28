# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# Example :
#
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# http://i.imgur.com/0qkUFco.png
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        stack = []
        res = 0
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                for j in range(A[i]-A[i-1]):
                    if len(stack) < 1: stack.append((+1,i))
                    v,k = stack[-1]
                    if v == -1:
                        stack.pop()
                        res += i-k
                    else: stack.append((+1,i))
            elif A[i] < A[i-1]:
                for j in range(A[i-1]-A[i]): stack.append((-1,i))
        return res


print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Sample Input :
#
# (1, 1)
# (2, 2)
# Sample Output :
#
# 2
# You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, X, Y):
        if len(X) < 3: return len(X)
        if all([True if X[i] == Y[i] == X[0] == Y[0] else False for i in range(len(X))]):
            return len(X)
        dic = {}
        for i in range(len(X)):
            for j in range(i+1,len(X)):
                funTuple = self.calculateFun((X[i], Y[i]), (X[j],Y[j]))
                if funTuple not in dic and funTuple: dic[funTuple] = 0
        maxPts = -1
        for k,v in dic.iteritems():
            for i in range(len(X)):
                # y = ax + b
                if k[0]*X[i]+k[1] == Y[i]:
                    dic[k] += 1
        for k,v in dic.iteritems():
            maxPts = max(maxPts, v)
        xes = {}
        for x in X:
            if x not in xes: xes[x] = 1
            else: xes[x] += 1
            maxPts = max(maxPts, xes[x])
        return maxPts

    def calculateFun(self, A, B):
        if A[0]-B[0] != 0:
            a = (A[1]-B[1]) / (A[0]*1.0 -B[0]) # (y1-y2)/(x1-x2)
        else:
            return
        b = A[1]-a*A[0] # y1-ax1
        return (a,b)


print Solution().maxPoints([-4, 0, 19], [-4, 7, -11])
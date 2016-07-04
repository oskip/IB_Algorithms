from collections import deque

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == B[0]:
                    if self.bfs(A, (i,j), B): return 1
        return 0

    def bfs(self, vals, start, target):
        q = deque()
        i, j = start
        q.append((1,i,j))
        targetPos = 1 # A position in a string of currently matched character

        while len(q) > 0:
            targetPos,i,j = q.popleft()
            if targetPos == len(target): return True
            if i-1 >= 0:
                if vals[i-1][j] == target[targetPos]: q.append((targetPos+1,i-1,j))
            if i+1 < len(vals):
                if vals[i+1][j] == target[targetPos]: q.append((targetPos+1,i+1,j))
            if j-1 >= 0:
                if vals[i][j-1] == target[targetPos]: q.append((targetPos+1,i,j-1))
            if j+1 < len(vals[i]):
                if vals[i][j+1] == target[targetPos]: q.append((targetPos+1,i,j+1))
        return False


print Solution().exist([ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ], "BCDCB")
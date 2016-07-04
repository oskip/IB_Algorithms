class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        n = len(A[0])
        dp = [0 for _ in range(n)]
        dp[n-1] = max(A[0][n-1], A[1][n-1])
        dp[n-2] = max(max(A[0][n-2], A[1][n-2]),dp[n-1])
        for i in reversed(range(n-2)):
            dp[i] = max(dp[i+2]+max(A[0][i],A[1][i]),dp[i+1])
        return dp[0]


print Solution().adjacent([
  [74, 37, 82, 1],
  [66, 38, 16, 1]
])
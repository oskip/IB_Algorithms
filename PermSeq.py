import math
class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        if k > math.factorial(n): return
        arr = range(1,n+1)
        res = []
        for i in xrange(1,n):
            index = 0
            pos = 0
            while index + math.factorial(n-i) < k:
                index += math.factorial(n-i)
                pos += 1
            res.append(str(arr[pos]))
            arr.remove(arr[pos])
            k -= index
        res.append(str(arr[0]))
        return ''.join(res)

print Solution().getPermutation(3, 7)

# 12345678910111213141516171819202122232425262728293031323335363839343740
# 12345678910111213141516171819202122232425262728293031323335363839343740

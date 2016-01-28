# You are given a string, S, and a list of words, L, that are all of the same length.
#
# Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
#
# Example :
#
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if len(B) < 1: return None
        l = len(B[0])
        n = len(B)
        if len(A) < l*n: return None
        dic = {}
        result = []
        for b in B:
            if b not in dic: dic[b] = 1
            else: dic[b] += 1
        tmpDic = dic.copy()
        for i, a in enumerate(A[0:len(A)-l*n+1]):
            sub = A[i:i+l*n]
            j = 0
            while j < l*n:
                word = sub[j:j+l]
                if word in tmpDic and tmpDic[word] > 0: tmpDic[word] -= 1
                else: break
                j += l
            if j == l*n: result.append(i)
            tmpDic = dic.copy()
        return result


print Solution().findSubstring("tbarfoocarmarmarmarmarcarfoofoocarbarfoomar", ["foo", "bar", "car", "mar"])

class Solution:
    def wordBreak(self, A, dic):
        self.dic = set(dic)
        self.res = []
        self.wordBreakRec(A,[],1)
        return self.res

    def wordBreakRec(self, s, curr, pos):
        if pos == len(s):
            if s in self.dic: self.res.append(curr+[s])
            return
        if s[0:pos] in self.dic:
            self.wordBreakRec(s[pos:], curr+[s[0:pos]], 0)
        self.wordBreakRec(s, curr, pos+1)

print Solution().wordBreak("aabbbabaaabbbabaabaab", ["bababbbb", "bbbabaa", "abbb",  "a", "aabbaab", "b", "babaabbbb", "aa", "bb" ])

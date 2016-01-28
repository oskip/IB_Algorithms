# Given a string s, partition s such that every string of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
#


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        self.res = []
        for i in xrange(1,len(A)+1):
            self.tryFindPali([],i,A)
        return self.res

    def tryFindPali(self,curr,l,s):
        if l == len(s) and self.isPali(s):
            self.res.append(curr+[s])
        elif l < len(s):
            if self.isPali(s[:l]):
                for i in xrange(1,len(s)+1):
                    self.tryFindPali(curr+[s[:l]],i,s[l:])

    def isPali(self, s):
        return s == s[::-1]

print Solution().partition("rardrar")
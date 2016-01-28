import math

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        alphabet = []
        n = len(A)

        for i, char in enumerate(A):
            alphabet.append(ord(char))

        alphabet = sorted(alphabet)
        rank = 0
        for i, char in enumerate(A):
            char = ord(char)

            maxRank = math.factorial(n-i)
            pos = alphabet.index(char)
            alphabet.remove(char)
            rank += maxRank*pos/(n-i)
        return (rank+1) % 1000003

print Solution().findRank('AaBbCc')

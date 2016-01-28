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

        duplicateCoeffs = {}
        ranks = {}
        for i, a in enumerate(alphabet):
            if a not in ranks:
                ranks[a] = i
            elif a in duplicateCoeffs:
                duplicateCoeffs[a] += 1
            else:
                duplicateCoeffs[a] = 2

        duplicateProduct = 1
        for dup in duplicateCoeffs.values():
            duplicateProduct *= math.factorial(dup)

        rank = 0
        for i, char in enumerate(A):
            char = ord(char)

            maxRank = math.factorial(n-i)/duplicateProduct
            pos = ranks[char]
            rank += maxRank*pos/(n-i)

            if char in duplicateCoeffs:
                duplicateCoeffs[char] -= 1
                duplicateProduct = 1
                for dup in duplicateCoeffs.values():
                    duplicateProduct *= math.factorial(dup)
            for a in ranks:
                if a > char:
                    ranks[a] -= 1

        return (rank+1) % 1000003

print Solution().findRank('aaacchfkihfiwkhfwkfhqhfnkjlriujlfaslfjslafjajewifjewilfjewlfajflhfhflskjasfljwaefkjlfafhoiahfahfiklkujkuriewruwiruwrehfsdyufkshfhmsyrmewahfabaaba')

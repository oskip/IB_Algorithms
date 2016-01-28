class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        start = 0
        stop = sum(C)*B
        while start <= stop:
            middle = (start+stop)/2
            canMiddle = self.canPaintInTime(middle, A, B, C)
            canPrevious = self.canPaintInTime(middle-1, A, B, C)
            if canMiddle and not canPrevious:
                return middle % 10000003
            elif canMiddle and canPrevious:
                stop = middle-1
            elif not canMiddle:
                start = middle+1

    def canPaintInTime(self, time, A, B, C):
        painterSum = 0
        i = 0
        while A > 0 and i < len(C):
            if C[i]*B > time: return False
            elif painterSum + C[i]*B <= time: painterSum += C[i]*B
            else:
                A -= 1
                if A == 0: break
                painterSum = C[i]*B
            i += 1
        if i == len(C): return True
        else: return False


# print Solution().canPaintInTime(104, 3, 2, [10, 20, 13, 23, 16, 22, 12, 18])

print Solution().paint(6, 10, [ 762, 798, 592, 899, 329  ])




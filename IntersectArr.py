class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        if len(A) == 0 or len(B) == 0: return []
        intersection = []
        j = 0
        i = 0
        while i < len(A):
            if A[i] == B[j]:
                intersection.append(A[i])
                j += 1
                i += 1
            elif A[i] > B[j]:
                j += 1
            else: i += 1
            if j >= len(B): return intersection
        return intersection


print Solution().intersect(
    [1, 5, 7, 8, 9, 10, 10, 14, 16, 16, 17, 19, 20, 20, 20, 20, 21, 23, 26, 27, 29, 30, 30, 30, 31, 32, 33, 33, 34, 35,
     35, 36, 37, 39, 39, 41, 42, 43, 43, 44, 44, 45, 46, 46, 47, 49, 51, 52, 53, 55, 55, 56, 57, 58, 59, 60, 65, 66, 66,
     68, 68, 69, 69, 70, 70, 70, 71, 73, 75, 75, 75, 79, 80, 80, 81, 82, 85, 87, 91, 92, 98, 98, 98, 99, 100, 101],
    [4, 7, 10, 10, 15, 17, 19, 20, 24, 27, 27, 30, 31, 35, 40, 41, 42, 46, 48, 49, 50, 51, 54, 57, 62, 62, 63, 66, 67,
     68, 69, 70, 71, 73, 74, 78, 80, 81, 92, 94, 99, 101])

#7 10 10 17 19 20 27 30 31 35 41 42 46 49 51 57 66 68 69 70 71 73 80 81 92 99 101
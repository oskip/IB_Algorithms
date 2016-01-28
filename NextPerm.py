class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if len(A) < 2: return A
        minA = min(A)
        for i in reversed(xrange(0, len(A)-1)):
            if A[i] < A[i+1]:
                minGreater = float('inf')
                minGreaterIndex = 0
                for j in xrange(i+1, len(A)):
                    if A[j] > A[i]:
                        minGreater = min(minGreater, A[j])
                        if minGreater == A[j]: minGreaterIndex = j
                A[i], A[minGreaterIndex] = A[minGreaterIndex], A[i]
                return A[:i+1] + sorted(A[i+1:])
        return sorted(A)

A = [ 444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52 ]
for i in range(0,10):
    A = Solution().nextPermutation(A)
    print A

# 444 994 508 72 125 299 181 238 354 223 691 249 838 890 758 675 424 199 201 788 609 582 979 259 901 371 766 759 983 728 220 16 158 822 515 488 846 321 908 469 84 460 961 285 417 142 952 626 916 247 116 975 202 734 128 312 499 274 213 208 472 265 315 335 205 784 708 681 160 448 365 165 190 693 606 226 351 241 526 311 164 98 422 363 103 747 507 669 153 856 701 695 52 319
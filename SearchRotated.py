class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = self.searchPivot(A)
        search1 = self.binarySearch(A[0:pivot], B)
        if search1 != -1: return search1
        search2 = self.binarySearch(A[pivot:], B)
        if search2 != -1: return search2+pivot
        return -1

    def searchPivot(self, A):
        n = len(A)
        start = 0
        stop = n-1
        while start <= stop:
            middle = (start+stop)/2
            if A[start] < A[stop]:
                return start
            if A[(middle-1+n)%n] > A[middle] and A[(middle+1)%n] > A[middle]:
                return middle
            elif A[start] <= A[middle]:
                start = middle+1
            elif A[middle] <= A[stop]:
                stop = middle-1

    def binarySearch(self, A, B):
        n = len(A)
        start = 0
        stop = n-1

        while start <= stop:
            middle = (start+stop)/2
            if A[middle] == B:
                return middle
            elif A[middle] < B:
                start = middle+1
            elif A[middle] > B:
                stop = middle-1
        return -1

print Solution().search([4, 5, 6, 7, 0, 1, 2], 12)

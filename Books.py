# N number of books are given.
# The ith book has Pi number of pages.
# You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated atleast one book.
#
# NOTE: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order.
#
# Input:
#  List of Books M number of students
#
# Your function should return an integer corresponding to the minimum number.
#
# Example:
#
# P : [12, 34, 67, 90]
# M : 2
#
# Output : 113
#
# There are 2 number of students. Books can be distributed in following fashion :
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student 2 with 67 + 90 = 157 pages
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
#
# Of the 3 cases, Option 3 has the minimum pages = 113.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A): return -1
        if B == len(A): return max(A)

        start = 0
        stop = sum(A)
        while start <= stop:
            middle = (start + stop)/2
            if not self.isValid(middle, A, B):
                start = middle+1
            elif self.isValid(middle, A, B) and not self.isValid(middle-1, A, B):
                return middle
            else:
                stop = middle-1

    def isValid(self, value, A, B):
        studentSum = 0
        for book in A:
            if book > value: return False
            elif studentSum + book <= value: studentSum += book
            else:
                B -= 1
                if B == 0: return False
                studentSum = book
        return True


print Solution().books([112, 312, 99, 121, 83, 152, 125, 773, 666, 331], 3)
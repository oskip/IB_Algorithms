# Given a singly linked list
#
#     L: L0 -> L1 -> ... -> Ln-1 -> Ln,
# reorder it to:
#
#     L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# You must do this in-place without altering the nodes values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        secArr = []
        firstArr = []
        n = self.length(A)
        if n < 3: return A
        i = n/2
        while n > 0:
            if n <= i: secArr.append(A)
            else: firstArr.append(A)
            n -= 1
            A = A.next
        head = firstArr[0]
        for j in range(0,len(firstArr)):
            if j > 0: secArr[len(secArr)-j].next = firstArr[j]
            if j < len(secArr):
                firstArr[j].next = secArr[len(secArr)-(j+1)]
                secArr[len(secArr)-(j+1)].next = None
            else: firstArr[j].next = None
        return head

    def length(self, A):
        i = 0
        while A:
            A = A.next
            i += 1
        return i

    # DRIVERS
    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.reorderList(headA)

res = Solution().runWithList([90, 94, 25, 51, 45, 29, 55, 63, 48, 27, 72, 10, 36, 68, 16, 20, 31, 7, 95, 70, 89, 23, 22, 9, 74, 71, 35, 5, 80, 11, 49, 92, 69, 6, 37, 84, 78, 28, 43, 64, 96, 57, 83, 13, 73, 97, 75, 59, 53, 52, 19, 18, 98, 12, 81, 24, 15, 60, 79, 34, 1, 54, 93, 65, 44, 4, 87, 14, 67, 26, 30, 77, 58, 85, 33, 21, 46, 82, 76, 88, 66, 101, 61, 47, 8 ])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)

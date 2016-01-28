# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        head = A
        n = self.length(A)
        secHeadPos = (n/2) if n%2 == 0 else (n/2 + 1)
        for i in range(0, secHeadPos):
            A = A.next
        revSecHead = self.reverse(A)
        revSec = revSecHead
        A = head
        for i in range(0,n/2):
            A.val = revSec.val - A.val
            revSec = revSec.next
            A = A.next
        sec = self.reverse(revSecHead)
        return head

    def length(self, A):
        i = 0
        while A:
            i += 1
            A = A.next
        return i

    def reverse(self, A):
        last = None
        while A:
            nxt = A.next
            A.next = last
            last = A
            A = nxt
        return last

    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.subtract(headA)

res = Solution().runWithList([95, 59, 26, 16, 31, 39, 29, 8, 74, 14, 41, 41, 64, 88, 34, 21, 67, 23, 17, 41, 3, 38, 4, 45, 93, 92, 99, 24])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)

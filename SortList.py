# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example :
#
# Input : 1 -> 5 -> 4 -> 3
#
# Returned list : 1 -> 2 -> 4 -> 5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        n = self.length(A)
        if n < 2: return A
        head = A
        secHead = A
        i = n/2
        while i > 0:
            nxt = secHead.next
            if i == 1: secHead.next = None
            secHead = nxt
            i -= 1
        head = self.sortList(head)
        secHead = self.sortList(secHead)
        return self.merge(head,secHead)

    def merge(self, head, secondHead):
        if head.val < secondHead.val:
            newHead = head
            head = head.next
        else:
            newHead = secondHead
            secondHead = secondHead.next
        newHeadSave = newHead
        while secondHead and head:
            if head.val < secondHead.val:
                newHead.next = head
                head = head.next
            else:
                newHead.next = secondHead
                secondHead = secondHead.next
            newHead = newHead.next
        while secondHead:
            newHead.next = secondHead
            secondHead = secondHead.next
            newHead = newHead.next
        while head:
            newHead.next = head
            head = head.next
            newHead = newHead.next
        return newHeadSave

    def length(self, A):
            i = 0
            while A:
                i += 1
                A = A.next
            return i

    # DRIVERS
    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.sortList(headA)

res = Solution().runWithList([5, 66, 68, 42, 73, 25, 84, 63, 72, 20, 77, 38, 8, 99, 92, 49, 74, 45, 30, 51, 50, 95, 56, 19, 31, 26, 98, 67, 100, 2, 24, 6, 37, 69, 11, 16, 61, 23, 78, 27, 64, 87, 3, 85, 55, 22, 33, 62])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)
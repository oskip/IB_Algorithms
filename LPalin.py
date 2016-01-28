# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        length = self.length(A)
        if length < 2: return 0
        j = length/2
        if length % 2 == 0: i = length/2
        else: i = length/2+1
        secondHead = A
        head = A
        while i > 0:
            secondHead = secondHead.next
            i -= 1
        while j > 0:
            j -= 1
            if j == 0: A.next = None
            A = A.next
        head = self.reverse(head)
        while head is not None and secondHead is not None:
            if head.val == secondHead.val:
                head = head.next
                secondHead = secondHead.next
            else: return 0
        if head is None and secondHead is None:
            return 1
        return 0

    def reverse(self, A):
        last = None
        while A != None:
            nxt = A.next
            A.next = last
            last = A
            A = nxt
        return last

    def length(self, A):
        i = 0
        while A is not None:
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
        return self.lPalin(headA)

print Solution().runWithList([1,2,3,4,3,2,1])
# output = []
# while res is not None:
#     output.append(str(res.val))
#     res = res.next
# print " -> ".join(output)
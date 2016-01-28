# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#  Note:
# * If n is greater than the size of the list, remove the first node of the list.
# Try doing it using constant additional space.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if A is None: return A
        B -= 1
        head = A
        ct = 0
        while A is not None:
            A = A.next
            ct += 1
        A = head
        i = min(max(ct-B,0),ct)
        if i <= 1: return head.next
        prev = head
        while i > 0:
            i -= 1
            if i == 0:
                prev.next = A.next
                break
            prev = A
            A = A.next
        return head

    def runWithList(self, A,B):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.removeNthFromEnd(headA,B)

res = Solution().runWithList([1,2,3,4,3,2,1],1)
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)



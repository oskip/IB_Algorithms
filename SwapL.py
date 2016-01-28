# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None or A.next is None: return A
        prev2 = None
        prev = A
        i = 1
        head = A.next
        A = A.next
        while A is not None:
            if i % 2 == 0:
                prev = A
            else:
                prev.next = A.next
                A.next = prev
                if prev2 is not None: prev2.next = A
                prev2 = prev
            i += 1
            A = prev.next
        return head
# DRIVERS
    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.swapPairs(headA)

res = Solution().runWithList([1,2,3,4,3,2,1])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)
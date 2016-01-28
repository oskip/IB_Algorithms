# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
#  Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list. Note 2:
# Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        head = A
        beforeRev = afterRev = None
        n -= 1
        while n > 0:
            n -= 1
            A = A.next
        last = A
        afterRev = A.next
        A = head
        m -= 1
        while m > 0:
            m -= 1
            if m == 0: beforeRev = A
            A = A.next
        first = A
        while A is not afterRev:
            nxt = A.next
            A.next = last
            last = A
            A = nxt
        beforeRev.next = last
        first.next = afterRev
        return head

# DRIVERS
    def runWithList(self, A,B,C):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.reverseBetween(headA,B,C)

res = Solution().runWithList([1,2,3,4,5,6,7,8],2,5)
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)
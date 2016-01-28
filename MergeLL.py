# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
#
# For example, given following linked lists :
#
#   5 -> 8 -> 20
#   4 -> 11 -> 15
# The merged list should be :
#
# 4 -> 5 -> 8 -> 11 -> 15 -> 20
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        nodes = []
        while A != None:
            nodes.append(A.val)
            A = A.next
        while B != None:
            nodes.append(B.val)
            B = B.next
        nodes = sorted(nodes)
        head = ListNode(nodes[0])
        previous = head
        for node in nodes[1:]:
            n = ListNode(node)
            previous.next = n
            previous = n
        return head

# DRIVERS
    def runWithList(self, A, B):
        headA = ListNode(A[0]) if len(A) > 0 else None
        headB = ListNode(B[0]) if len(B) > 0 else None
        lA = headA
        lB = headB
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        for b in B[1:]:
            e = ListNode(b)
            lB.next = e
            lB = e
        return self.mergeTwoLists(headA, headB)

res = Solution().runWithList([1,2,3,4,3,5], [])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)

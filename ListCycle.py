class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        cycleTo = None
        nodes = set([])
        while A:
            if A not in nodes:
                nodes.add(A)
                A = A.next
            else:
                cycleTo = A
                break
        return cycleTo
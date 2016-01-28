# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if self.length(A) > self.length(B): A, B = B, A
        head = A
        carry = 0
        while A and B:
            res = A.val + B.val + carry
            A.val = res%10
            carry = 1 if res > 9 else 0
            if A.next is None: tail = A
            A = A.next
            B = B.next
        A = tail
        while B:
            res = B.val + carry
            A.next = ListNode(res%10)
            carry = 1 if res > 9 else 0
            A = A.next
            B = B.next
        if carry == 1:
            A.next = ListNode(1)
        return head

    def length(self, A):
        i = 0
        while A is not None:
            A = A.next
            i += 1
        return i
# Reverse a linked list. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL,
#
# return 5->4->3->2->1->NULL.
#
# PROBLEM APPROACH :
#
# Complete solution code in the hints

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A == None: return None
        head = A
        previous = A
        A = A.next
        while A != None:
            nextEl = A.next
            self.delete(A, previous)
            head = self.insertAtHead(A, head)
            A = nextEl
        return head

    def insertAtHead(self, node, head):
        node.next = head
        return node

    def delete(self, node, previous):
        previous.next = node.next
        node.next = None
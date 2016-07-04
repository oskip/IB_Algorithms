class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def length(self, head):
        l = 0
        while head is not None:
            l+= 1
            head = head.next
        return l

    def reverse(self, head):
        curr = None
        while head is not None:
            nxt = head.next
            head.next = curr
            curr = head
            head = nxt
        return curr

    def checkPal(self, head):
        l = self.length(head)
        if l < 2: return True
        n = l/2-1 + l%2
        curr = head
        while n>0:
            curr = curr.next
            n -= 1
        s = curr.next
        curr.next = None
        s = self.reverse(s)
        curr = head
        n = self.length(s)
        while n>0:
            if s.val != curr.val: return False
            s = s.next
            curr = curr.next
            n -= 1
        return True

 # DRIVERS
    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.checkPal(headA)


res = Solution().runWithList([i for i in range(10)] + [12] + [(9-i) for i in range(10)])
print res
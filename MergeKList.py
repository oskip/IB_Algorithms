# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, lists):
        vals = []
        for h in lists:
            while h is not None:
                vals.append(h.val)
                h = h.next
        vals = sorted(vals)
        head = res = None
        for e in vals:
            if not head:
                head = ListNode(e)
                res = head
            else:
                head.next = ListNode(e)
                head = head.next
        return res

# DRIVERS
    def runWithList(self, lists):
        res = []
        for h in lists:
            headA = ListNode(h[0]) if len(h) > 0 else None
            lA = headA
            for a in h[1:]:
                e = ListNode(a)
                lA.next = e
                lA = e
            res.append(headA)
        return self.mergeKLists(res)

print Solution().runWithList([[1,2,3,4,3,2,1], [3,2,3,4,1]])
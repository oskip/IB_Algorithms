# Sort a linked list using insertion sort.
#
# We have explained Insertion Sort at Slide 7 of Arrays
#
# Insertion Sort Wiki has some details on Insertion Sort as well.
#
# Example :
#
# Input : 1 -> 3 -> 2
#
# Return 1 -> 2 -> 3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A is None: return None
        if A.next is None: return A
        head = A
        lastSorted = A
        curr = A.next
        while curr is not None:
            pt = head
            A = A.next
            if pt.val > curr.val:
                lastSorted.next = lastSorted.next.next if lastSorted.next is not None else None
                curr.next = head
                head = curr
            elif curr.val >= lastSorted.val:
                lastSorted = curr
            else:
                while pt is not lastSorted:
                    if pt.val <= curr.val <= pt.next.val:
                        lastSorted.next = lastSorted.next.next if lastSorted.next is not None else None
                        curr.next = pt.next
                        pt.next = curr
                        break
                    pt = pt.next
            curr = lastSorted.next
        lastSorted.next = None
        return head

    def runWithList(self, A):
        headA = ListNode(A[0]) if len(A) > 0 else None
        lA = headA
        for a in A[1:]:
            e = ListNode(a)
            lA.next = e
            lA = e
        return self.insertionSortList(headA)

res = Solution().runWithList([45, 43, 7, 19, 88, 8, 98, 72, 35, 87, 48, 12, 39, 89 ])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)
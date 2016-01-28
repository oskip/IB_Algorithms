class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        prev = None
        while A is not None:
            tmp = A
            val = A.val
            ct = 0
            while A is not None and val == A.val:
                A = A.next
                ct += 1
            if ct > 1:
                if prev is not None: prev.next = A
                else: head = A
            else: prev = tmp
        return head
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def kthToTheLast(k, head):
    if not head: return
    a = b = head

    while k > 0 and b.next:
        k -= 1
        b = b.next
    # k was >= length of the linked list
    if not b.next: return a
    while b.next:
        a = a.next
        b = b.next
    return a


# DRIVERS
def runWithList(arg, A):
    headA = Node(A[0]) if len(A) > 0 else None
    lA = headA
    for a in A[1:]:
        e = Node(a)
        lA.next = e
        lA = e
    return kthToTheLast(arg, headA)


res = runWithList(11, [1,2,3,3,2,4,5,1,2,3,11])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)

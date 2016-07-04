class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def removeDuplicates(A):
    newList = A
    head = newList
    values = {A.val}
    while A.next:
        if A.next.val not in values:
            newList.next = A.next
            values.add(A.next.val)
            newList = newList.next
        A = A.next

    return head


# DRIVERS
def runWithList(A):
    headA = Node(A[0]) if len(A) > 0 else None
    lA = headA
    for a in A[1:]:
        e = Node(a)
        lA.next = e
        lA = e
    return removeDuplicates(headA)


res = runWithList([1,2,3,3,2,4,5,1,2,3,11])
output = []
while res is not None:
    output.append(str(res.val))
    res = res.next
print " -> ".join(output)
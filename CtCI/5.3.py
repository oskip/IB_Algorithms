def swapBits(A):
    i = 1
    while i < 32:
        IBit = (A >> i) & 1
        prevIBit = (A >> i - 1) & 1
        A = setBit(A, i - 1, IBit)
        A = setBit(A, i, prevIBit)
        i += 2
    return A


def setBit(A, i, v):
    mask = ~(1 << i)
    return (A & mask) | v << i



n = 48903242
sn = swapBits(n)
print list(bin(n))
print list(bin(sn))
def kthNumber(k):
    x = 3
    y = 5
    z = 7
    for step in range(k - 1):
        moreX = 3 * x * y * z
        moreY = x * 5 * y * z
        moreZ = x * y * 7 * z
        if moreX <= moreY and moreX <= moreZ:
            x *= 3
        elif moreY < moreX and moreY <= moreZ:
            y *= 5
        elif moreZ < moreY and moreZ < moreX:
            z *= 7
    return x*y*z


results = [kthNumber(i) for i in range(1, 100)]
chck = []
for i1 in range(1,20):
    for i2 in range(1,20):
        for i3 in range(1,20):
            chck.append(3 ** i1 * 5 ** i2 * 7 ** i3)
print results
print sorted(chck)

# Check if sorted
maxVal = results[0]
for r in results[1:]:
    maxVal = max(r, maxVal)
    if maxVal != r: raise Exception("error")

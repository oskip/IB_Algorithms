def compressString(S):
    if len(S) == 0: return S
    lastChar = S[0]
    lastCharCt = 1
    i = 1
    charArr = []
    while i < len(S):
        if S[i] == lastChar:
            lastCharCt += 1
        else:
            charArr.append((lastChar,str(lastCharCt)))
            lastChar = S[i]
            lastCharCt = 1
        i += 1
    charArr.append((lastChar,lastCharCt))
    result = "".join([ch+str(ct) for ch,ct in charArr])
    if len(S) <= len(result):
        result = S
    return result

print compressString("aabcccccaaa")

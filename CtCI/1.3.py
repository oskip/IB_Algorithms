def isPermutation(S1, S2):
    if len(S1) != len(S2): return False
    charArr = [0]*255
    for s in S1:
        if (ord(s)) > 255: return
        charArr[ord(s)] += 1
    for s in S2:
        if (ord(s)) > 255: return
        charArr[ord(s)] -= 1
    return sum(charArr) == 0

print isPermutation("jdljfskl","fljksjld")

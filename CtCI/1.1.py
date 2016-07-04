# coding=utf-8
def isUnique(S):
    S = sorted(S)
    i = 1
    while i < len(S):
        if S[i] == S[i-1]:
            return False
        i += 1  # O tym zapomniałem
    return True


def isUnique2(S):
    chars = {}
    for s in S:
        if s in chars: return False
        else: chars[s] = True
    return all([e == 1 for k, e in chars.iteritems()])


S = "abstrkcj"
print isUnique(S), isUnique2(S)
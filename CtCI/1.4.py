def replaceSpaces(S):
    if len(S) == 0: return S
    S = list(S)
    spaces = 0
    i = len(S) - 1
    while S[i] == " " and i > 0:
        i -= 1
    lastCharPos = i
    for i in reversed(range(lastCharPos + 1)):
        if S[i] == " ":
            spaces += 1
    for i in reversed(range(lastCharPos + 1)):
        if S[i] != " ":
            S[i + spaces * 2] = S[i]
        else:
            spaces -= 1
            S[i + spaces*2], S[i + 1 + spaces*2], S[i + 2 + spaces*2] = '%', '2', '0'
    return ''.join(S)


print replaceSpaces("Mr John Smith is a bitch          ")

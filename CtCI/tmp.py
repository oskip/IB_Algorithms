class VowelReverser(object):
    def __init__(self):
        self.vowels = {"a", "o", "e", "y", "i", "u"}

    def reverse(self, S):
        S_list = list(S)
        vowels_indicies = []
        for i in range(len(S_list)):
            if S_list[i] in self.vowels:
                vowels_indicies.append(S_list[i])
        vowels_indicies = vowels_indicies[::-1]
        j = 0
        for i in range(len(S_list)):
            if S_list[i] in self.vowels:
                S_list[i] = vowels_indicies[j]
                j += 1
        return "".join(S_list)

print VowelReverser().reverse("hello")
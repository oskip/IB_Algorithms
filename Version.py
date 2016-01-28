# Compare two version numbers version1 and version2.
#
# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        Anums = [int(a) for a in A.split(".")]
        Bnums = [int(b) for b in B.split(".")]
        to = len(Anums)
        for a in reversed(Anums):
            if a == 0: to -= 1
            else: break
        Anums = Anums[0:to]
        to = len(Bnums)
        for b in reversed(Bnums):
            if b == 0: to -= 1
            else: break
        Bnums = Bnums[0:to]
        i = 0

        while i < min(len(Anums), len(Bnums)):
            if int(Anums[i]) > int(Bnums[i]): return 1
            elif int(Anums[i]) < int(Bnums[i]): return -1
            i += 1

        if len(Anums) > len(Bnums): return 1
        elif len(Anums) < len(Bnums): return -1
        else: return 0


print Solution().compareVersion("1.0", "1")
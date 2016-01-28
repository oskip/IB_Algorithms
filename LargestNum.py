class Solution:

    def comparator(self, x, y):
        xStr = str(x)
        yStr = str(y)
        con = (xStr+yStr).lstrip("0")
        con2 = (yStr+xStr).lstrip("0")
        if con == "": con = "0"
        if con2 == "": con2 = "0"

        if int(con) > int(con2):
            return -1
        elif int(con) < int(con2):
            return 1
        return 0

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, cmp=self.comparator)
        result = "".join(str(i) for i in A)
        result = result.lstrip("0")
        "".join(result.split())
        if result == "": return "0"
        else: return result


print Solution().largestNumber([ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ])

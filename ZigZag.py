# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# **Example 2 : **
# ABCD, 2 can be written as
#
# A....C
# ...B....D
# and hence the answer would be ACBD.


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1: return A
        lines = [""] * B
        i = 0
        up = True
        for c in A:
            lines[i] += c
            if up:
                i += 1
            else:
                i -= 1
            if i < 0:
                i = 1
                up = True
            elif i >= B:
                i = B - 2
                up = False
        result = ""
        for line in lines:
            result += "".join(line)
        return result


print Solution().convert("kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS", 4)

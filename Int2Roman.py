# Please Note:
#
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
#
# Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Example :
#
# Input : 5
# Return : "V"
#
# Input : 14
# Return : "XIV"
#  Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all
# the needed clarifications and see the expected response using "See Expected Output" For the purpose of this question,
# https://projecteuler.net/about=roman_numerals has very detailed explanations.


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        romans = {1: "I", 2: "II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
                20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
                100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
                1000:"M", 2000:"MM", 3000:"MMM"}
        result = ""
        i = 1
        while A > 0:
            index = (A % 10)*i
            if index != 0:
                result = romans[index] + result
            A /= 10
            i *= 10
        return result
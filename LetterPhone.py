# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png
#
# The digit 0 maps to 0 itself.
# The digit 1 maps to 1 itself.
#
# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Make sure the returned strings are lexicographically sorted.


class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        arr = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        l = []
        self.combination(arr, l, "", A)
        return l

    def combination(self, arr, l, curr, A):
        if len(A) == 0:
            l.append(curr)
            return
        num = A[0]
        A = A[1:]
        for s in arr[int(num)]:
            self.combination(arr, l, curr+s, A)

print Solution().letterCombinations("110")
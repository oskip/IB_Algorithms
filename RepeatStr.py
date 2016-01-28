# Given a string,
# find the length of the longest substring without repeating characters.
#
# Example:
#
# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#
# For "bbbbb" the longest substring is "b", with the length of 1.


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if len(A) == 1: return 1
        letters = {}
        maxLen = start = stop = 0
        while stop < len(A):
            if A[stop] in letters:
                maxLen = max(maxLen, stop-start)
                start = letters[A[stop]]+1
                for k in letters.keys():
                    if letters[k] < start: del letters[k]
                letters[A[stop]] = stop
                stop += 1
            else:
                letters[A[stop]] = stop
                stop += 1
        maxLen = max(maxLen, stop-start)
        return maxLen

print Solution().lengthOfLongestSubstring("dadbc")
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
# Note that when the count of a character C in T is N, then the count of C in minimum window in S should be atleast N.
#
# Example :
#
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC"
#
#  Note:
# If there is no such window in S that covers all characters in T, return the empty string ''.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).


class Solution:
    # @param S : string
    # @param T : string
    # @return a string
    def minWindow(self, S, T):
        lookingFor = {}
        for t in T:
            if t not in lookingFor: lookingFor[t] = 1
            else: lookingFor[t] += 1
        found = {}
        minWindow = 2 ** 31
        start = stop = ct = 0
        result = ""
        while stop < len(S):
            if S[stop] not in lookingFor:
                stop += 1
                continue
            if S[stop] not in found: found[S[stop]] = 1
            else: found[S[stop]] += 1
            if found[S[stop]] <= lookingFor[S[stop]]: ct += 1
            if ct == len(T):
                while S[start] not in lookingFor or found[S[start]] > lookingFor[S[start]]:
                    if S[start] in found and found[S[start]] > lookingFor[S[start]]: found[S[start]] -= 1
                    start += 1
                windowLen = stop-start + 1
                if windowLen < minWindow:
                    minWindow = windowLen
                    result = S[start:stop+1]
            stop += 1
        return result


print Solution().minWindow(
    "xiEjBOGeHIMIlslpQIZ6jERaAVoHUc9Hrjlv7pQpUSY8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0BrmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9BbkNsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5uq1IxhAYZvRQVHtuHae0xxwCbRh6S7fCLKfXeSFITfKHnLdT65K36vGC7qOEyyT0Sm3Gwl2iXYSN2ELIoITfGW888GXaUNebAr3fnkuR6VwjcsPTldQSiohMkkps0MH1cBedtaKNoFm5HbH15kKok6aYEVsb6wOH2w096OwEyvtDBTQwoLN87JriLwgCBBavbOAiLwkGGySk8nO8dLHuUhk9q7f0rIjXCsQeAZ1dfFHvVLupPYekXzxtWHd84dARvv4Z5L1Z6j8ur2IXWWbum8lCi7aErEcq41WTo8dRlRykyLRSQxVH70rUTz81oJS3OuZwpI1ifBAmNXoTfznG2MXkLtFu4SMYC0bPHNctW7g5kZRwjSBKnGihTY6BQYItRwLUINApd1qZ8W4yVG9tnjx4WyKcDhK7Ieih7yNl68Qb4nXoQl079Vza3SZoKeWphKef1PedfQ6Hw2rv3DpfmtSkulxpSkd9ee8uTyTvyFlh9G1Xh8tNF8viKgsiuCZgLKva32fNfkvW7TJC654Wmz7tPMIske3RXgBdpPJd5BPpMpPGymdfIw53hnYBNg8NdWAImY3otYHjbl1rqiNQSHVPMbDDvDpwy01sKpEkcZ7R4SLCazPClvrx5oDyYolubdYKcvqtlcyks3UWm2z7kh4SHeiCPKerh83bX0m5xevbTqM2cXC9WxJLrS8q7XF1nh",
    "dO4BRDaT1wd0YBhH88Afu7CI4fwAyXM8pGoGNsO1n8MFMRB7qugS9EPhCauVzj7h")


# 8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0BrmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9BbkNsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5uq1IxhAYZvR

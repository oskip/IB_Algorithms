# Given a collection of intervals, merge all overlapping intervals.
#
# For example:
#
# Given [1,3],[2,6],[8,10],[15,18],
#
# return [1,6],[8,10],[15,18].
#
# Make sure the returned intervals are sorted.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        intervals = [Interval(s, e) for (s,e) in intervals]
        intervals.sort(key=lambda interval: interval.start)
        BIG_NUMBER = 9999999999999
        merged = []
        wereMerged = False
        newL = BIG_NUMBER
        newR = 0

        for i in xrange(1, len(intervals)):
            interval = intervals[i]
            previous = intervals[i-1]
            if min(interval.end, previous.end) >= max(interval.start, previous.start):
                merged.append(interval)
                newL = min(newL, previous.start)
                newR = max(newR, interval.end, previous.end)
                if not wereMerged:
                    merged.append(previous)
                wereMerged = True

            elif wereMerged:
                intervals.insert(i, Interval(newL, newR))
                wereMerged = False
                newL = BIG_NUMBER
                newR = 0

        if wereMerged:
            intervals.append(Interval(newL, newR))

        for interval in merged:
            intervals.remove(interval)

        print [(interval.start, interval.end) for interval in intervals]

Solution().merge([(54, 75), (56, 60), (61, 86), (22, 43), (56, 87), (32, 53), (14, 81), (64, 65), (9, 42), (12, 33), (22, 58), (84, 90), (27, 59), (41, 48), (43, 47), (22, 29), (16, 23), (41, 72), (15, 87), (20, 59), (45, 84), (14, 77), (72, 93), (20, 58), (47, 53), (25, 88), (5, 89), (34, 97), (14, 47)])

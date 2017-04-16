# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        data = []
        for i, interval in enumerate(intervals):
            data.append((interval.start, True, i))
            data.append((interval.end, False, i))
        data.sort()
        ri = {}
        n = len(data)
        sp = ep = 0
        while ep < n:
            if data[ep][1]:
                ep += 1
            if sp < ep:
                sp = ep + 1
            while sp < n and not data[sp][1]:
                sp += 1
            ri[data[ep][2]] = data[sp][2] if sp < n else -1
            ep += 1
        return [ri[i] for i in range(len(intervals))]

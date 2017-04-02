class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        s = set()
        for t in timePoints:
            t = convert(t)
            if t in s:
                return 0
            s.add(t)
            s.add(t + 1440)
        last = -1
        ret = 3000
        for t in sorted(s):
            if last == -1:
                last = t
                continue
            if t - last < ret:
                ret = t - last
            last = t
        return ret
        
def convert(t):
    hour, minute = t.split(':')
    return int(hour) * 60 + int(minute)

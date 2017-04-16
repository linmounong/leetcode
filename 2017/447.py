import collections

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return sum(cnt * (cnt - 1) for x1, y1 in points for cnt in collections.Counter((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) for x2, y2 in points).itervalues() if cnt > 1)

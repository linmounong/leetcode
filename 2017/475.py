class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        i = 0
        ret = 0
        n = len(heaters)
        for h in houses:
            while i + 1 < n and heaters[i + 1] < h:
                i += 1
            t = abs(heaters[i] - h)
            if i + 1 < n and heaters[i + 1] - h < t:
                t = heaters[i + 1] - h
            if t > ret:
                ret = t
        return ret

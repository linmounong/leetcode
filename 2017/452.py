import heapq

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        hl = [(p[0], i) for i, p in enumerate(points)]
        hr = [(p[1], i) for i, p in enumerate(points)]
        heapq.heapify(hl)
        heapq.heapify(hr)
        ret = 0
        s = set()
        while hr:
            r, i = heapq.heappop(hr)
            if i in s:
                continue
            ret += 1
            while hl and hl[0][0] <= r:
                s.add(heapq.heappop(hl)[1])
        return ret

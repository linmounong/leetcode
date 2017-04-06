class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total / n
        ret = 0
        l = 0
        ll = 0
        r = total
        rr = total
        for machine in machines:
            r -= machine
            rr -= avg
            if l <= ll and r <= rr:
                ret = max(ret, ll - l + rr - r)
            else:
                ret = max(ret, abs(ll - l), abs(rr - r))
            l += machine
            ll += avg
        return ret

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not duration:
            return 0
        ret = 0
        poisoned_until = 0
        for t in timeSeries:
            if t > poisoned_until:
                poisoned_until = t
            new_poisoned_until = t + duration
            ret += new_poisoned_until - poisoned_until
            poisoned_until = new_poisoned_until
        return ret

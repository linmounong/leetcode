class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        ret = 0
        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
                ret = max(cnt, ret)
        return ret

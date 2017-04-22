class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def doable(s):
            n = 1
            subsum = 0
            for num in nums:
                subsum += num
                if subsum > s:
                    n += 1
                    if n > m:
                        return False
                    subsum = num
            return True
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) / 2
            if doable(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                ret.append(i + 1)
            else:
                nums[i] *= -1
        return ret

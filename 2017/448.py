class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in xrange(n):
            j = nums[i] % n - 1
            nums[j] += n
        return [i + 1 for i in xrange(n) if nums[i] <= n]

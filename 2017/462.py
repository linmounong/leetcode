class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        uppermedian = nums[len(nums) / 2]
        return sum(abs(num - uppermedian) for num in nums)

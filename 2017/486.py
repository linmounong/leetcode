class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = {}
        def foo(i, j):
            if i >= j:
                return 0
            if i == j - 1:
                return nums[i]
            if i == j - 2:
                return max(nums[i], nums[i + 1])
            if (i, j) not in memo:
                memo[i, j] = max(nums[i] + min(foo(i + 2, j),
                                               foo(i + 1, j - 1)),
                                 nums[j - 1] + min(foo(i, j - 2),
                                                   foo(i + 1, j - 1)))
            return memo[i, j]
        return foo(0, n) >= (sum(nums) / 2.0)

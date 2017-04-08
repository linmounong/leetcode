class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        memo = [{} for _ in nums]  # memo[i][j] -> ways for nums[i:] to get sum j
        def foo(i, j):
            if i == n:
                return 1 if j == 0 else 0
            if j not in memo[i]:
                memo[i][j] = foo(i + 1, j - nums[i]) + foo(i + 1, j + nums[i])
            return memo[i][j]
        return foo(0, S)
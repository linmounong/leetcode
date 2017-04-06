class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {score: i for i, score in enumerate(nums)}
        for rank, score in enumerate(sorted(nums, reverse=True)):
            i = d[score]
            if rank == 0:
                nums[i] = "Gold Medal"
            elif rank == 1:
                nums[i] = "Silver Medal"
            elif rank == 2:
                nums[i] = "Bronze Medal"
            else:
                nums[i] = str(rank + 1)
        return nums

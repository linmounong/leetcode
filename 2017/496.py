class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pos = {num: i for i, num in enumerate(nums)}
        memo = {}
        def nge(i):
            if i not in memo:
                j = i + 1
                while 0 <= j < n and nums[i] > nums[j]:
                    j = nge(j)
                memo[i] = j
            return memo[i]
        ret = []
        for num in findNums:
            i = pos[num]
            i = nge(i)
            ret.append(nums[i] if 0 <= i < n else -1)
        return ret

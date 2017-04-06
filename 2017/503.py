class Solution(object):

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.extend(nums)
        l = [None for _ in range(2 * n)]
        for i in range(len(nums) - 1, -1, -1):
            j = i + 1
            while 0 < j < 2 * n:
                if nums[j] > nums[i]:
                    break
                j = l[j]
            else:
                j = -1
            l[i] = j
        return [nums[i] if i >= 0 else -1 for i in l[:n]]

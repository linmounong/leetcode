class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                if num & 2**i:
                    t[i] += 1
        n = len(nums)
        return sum(m * (n - m) for m in t)

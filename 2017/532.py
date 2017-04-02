class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        if k == 0:
            return sum(count >= 2 for count in counts.values())
        return sum((num + k) in counts for num in counts)

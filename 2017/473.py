class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False
        total = sum(nums)
        if total % 4:
            return False
        target = total / 4
        matches = {}
        for num in nums:
            matches[num] = matches.get(num, 0) + 1
        matches = [[match, cnt] for match, cnt in matches.iteritems()]
        matches.sort(key=lambda o: -o[0])
        def foo(side, length, i):
            if side == 3:
                return True
            if length == target:
                return foo(side + 1, 0, 0)
            if i == len(matches):
                return False
            maxn = min((target - length) / matches[i][0], matches[i][1])
            for n in reversed(range(maxn + 1)):
                matches[i][1] -= n
                if foo(side, length + n * matches[i][0], i + 1):
                    return True
                matches[i][1] += n
            return False
        matches[0][1] -= 1
        return foo(0, matches[0][0], 0)

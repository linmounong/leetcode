class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        k = maxChoosableInteger
        n = desiredTotal
        if k * (k + 1) / 2 < n:
            return False
        memo = {}
        state = range(1, k + 1)
        indices = range(k)[::-1]
        def foo(m):
            key = str(state)
            if key in memo:
                return memo[key]
            for i in indices:
                if not state[i]:
                    continue
                tmp = state[i]
                if tmp >= m:
                    memo[key] = True
                    return True
                state[i] = 0
                will_lose = foo(m - tmp)
                state[i] = tmp
                if not will_lose:
                    memo[key] = True
                    return True
            memo[key] = False
            return False
        return foo(n)

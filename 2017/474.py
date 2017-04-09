class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        blacklist = []
        strs.sort(key=len)
        def foo(i, m, n, cnt):
            if i >= len(strs):
                return cnt
            s = strs[i]
            zero = s.count('0')
            one = len(s) - zero
            if zero > m or one > n:
                if zero <= m or one <= n:
                    cnt = max(cnt, foo(i + 1, m, n, cnt))
                return cnt
            for x, y in blacklist:
                if x <= zero and y <= one:
                    return foo(i + 1, m, n, cnt)
            a = foo(i + 1, m - zero, n - one, cnt + 1)

            blacklist.append((zero, one))
            b = foo(i + 1, m, n, cnt)
            blacklist.pop()
            return max(a, b)
        return foo(0, m, n, 0)

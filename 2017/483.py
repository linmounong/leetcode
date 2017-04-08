import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = long(n)
        def foo(k):
            x = long(math.pow(n, 1.0 / k))
            m = 1
            while k:
                m = m * x + 1
                k -= 1
            if m == n:
                return x
        for k in range(int(math.log(n, 2)), 1, -1):
            x = foo(k)
            if x is not None:
                return str(x)
        return str(n - 1)

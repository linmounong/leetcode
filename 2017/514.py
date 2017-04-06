class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        # memo[i][j] == steps needed from ring[i] to finish key[j:]
        memo = [[None for _ in xrange(len(key))] for _ in xrange(n)]
        # left[i][c] == steps to the first c on the left (rotate) from ring[i]
        left = [{} for _ in xrange(n)]
        # right[i][c] == steps to the first c on the right (rotate) from ring[i]
        right = [{} for _ in xrange(n)]
        def findleft(i, c):
            if c not in left[i]:
                left[i][c] = ring.rfind(c, 0, i + 1)
                if left[i][c] < 0:
                    left[i][c] = ring.rfind(c, i + 1)
            return left[i][c]
        def findright(i, c):
            if c not in right[i]:
                right[i][c] = ring.find(c, i)
                if right[i][c] < 0:
                    right[i][c] = ring.find(c)
            return right[i][c]
        def foo(i, j):
            if j == len(key):
                return 0
            if memo[i][j] is None:
                c = key[j]
                il = findleft(i, c)
                stepl = i - il
                if stepl < 0:
                    stepl += n
                ir = findright(i, c)
                stepr = ir - i
                if stepr < 0:
                    stepr += n
                memo[i][j] = min(stepl + foo(il, j+1), stepr + foo(ir, j+1)) + 1
            return memo[i][j]
        return foo(0, 0)

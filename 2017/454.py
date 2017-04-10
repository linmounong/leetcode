class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        n = len(A)
        d = {}
        ret = 0
        for i in range(n):
            for j in range(n):
                s = A[i] + B[j]
                d[s] = d.get(s, 0) + 1
        for i in range(n):
            for j in range(n):
                s = -C[i] - D[j]
                if s in d:
                    ret += d[s]
        return ret

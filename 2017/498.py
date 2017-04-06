class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if not n:
            return []
        m = len(matrix[0])
        if not m:
            return []
        d1 = ((-1, 1), (1, 0), (1, -1))
        d2 = ((1, -1), (0, 1), (-1, 1))
        d = (d1, d2)
        i = j = 0
        downleft = False
        ret = []
        while True:
            ret.append(matrix[i][j])
            if i == n - 1 and j == m - 1:
                break
            dx = d[downleft]
            i += dx[0][0]
            j += dx[0][1]
            if not (0 <= i < n and 0 <= j < m):
                downleft = not downleft
                i += dx[1][0]
                j += dx[1][1]
                if not (0 <= i < n and 0 <= j < m):
                    i += dx[2][0]
                    j += dx[2][1]
        return ret

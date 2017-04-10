class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        def is_land(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j]
        ret = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y]:
                    for i, j in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
                        if not is_land(i, j):
                            ret += 1
        return ret

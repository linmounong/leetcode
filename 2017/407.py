import heapq

class Solution(object):
  def trapRainWater(self, heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    n = len(heightMap)
    if n < 3:
      return 0
    m = len(heightMap[0])
    if m < 3:
      return 0
    h = []
    s = set()
    for j in range(m):
      h.append((heightMap[0][j], 0, j))
      h.append((heightMap[n-1][j], n-1, j))
      s.add((0, j))
      s.add((n-1, j))
    for i in range(1, n - 1):
      h.append((heightMap[i][0], i, 0))
      h.append((heightMap[i][m-1], i, m-1))
      s.add((i, 0))
      s.add((i, m-1))
    heapq.heapify(h)
    ret = [0]
    while h:
      height, i, j = heapq.heappop(h)
      def foo(i, j):
        if not (0 <= i < n and 0 <= j < m and (i, j) not in s):
          return 
        s.add((i, j))
        if heightMap[i][j] > height:
          heapq.heappush(h, (heightMap[i][j], i, j))
          return
        ret[0] += height - heightMap[i][j]
        foo(i+1, j)
        foo(i-1, j)
        foo(i, j+1)
        foo(i, j-1)
      foo(i+1, j)
      foo(i-1, j)
      foo(i, j+1)
      foo(i, j-1)
    return ret[0]

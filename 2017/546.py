import itertools
class Solution(object):
  def removeBoxes(self, boxes):
    """
    :type boxes: List[int]
    :rtype: int
    """
    boxes = [(k, len(list(g))) for (k, g) in itertools.groupby(boxes)]
    n = len(boxes)
    mem = [[[None] * 100 for _ in range(n)] for _ in range(n)]
    def foo(i, j, k):
      if i > j:
        return 0
      if mem[i][j][k] is None:
        k2 = boxes[j][1] + k
        val = foo(i, j - 1, 0) + k2 * k2
        for h in range(i, j):
          if boxes[h][0] == boxes[j][0]:
            val = max(val, foo(i, h, k2) + foo(h + 1, j - 1, 0))
        mem[i][j][k] = val
      return mem[i][j][k]
    return foo(0, n-1, 0)
# 
# s = Solution()
# boxes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print s.removeBoxes(boxes)

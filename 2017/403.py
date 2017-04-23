class Solution(object):
  def canCross(self, stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    n = len(stones)
    dp = [{} for _ in stones]
    def foo(i, j):
      if i == n - 1:
        return True
      if j in dp[i]:
        return dp[i][j]
      cand = []
      nexti = i + 1
      while nexti < n:
        nextj = stones[nexti] - stones[i]
        if nextj > j + 1:
          break
        if nextj in (j - 1, j, j + 1):
          cand.append((nexti, nextj))
        nexti += 1
      for nexti, nextj in reversed(cand):
        if foo(nexti, nextj):
          dp[i][j] = True
          break
      else:
        dp[i][j] = False
      return dp[i][j]
    return foo(0, 0)
# 
# s = Solution()
# print s.canCross([0,1,3,5,6,8,12,17])

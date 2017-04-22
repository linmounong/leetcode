class Solution(object):
  def longestPalindromeSubseq(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    memo = [[0] * n for _ in range(n)]
    def dbg():
        for line in memo:
          print line
    def foo(i, j):
      if i > j:
        return 0
      if i == j:
        return 1
      if not memo[i][j]:
        l = i
        r = j
        cnt = 0
        while l < r and s[l] == s[r]:
          cnt += 2
          l += 1
          r -= 1
        if l == r:
          memo[i][j] = cnt + 1
        else:
          val = cnt + foo(l, r - 1)
          if l < r:
            k = s.find(s[r], l, r)
            if k != -1:
              val = max(val, foo(k + 1, r - 1) + 2 + cnt)
          memo[i][j] = val
      return memo[i][j]
    return foo(0, n - 1)

if __name__ == '__main__':
  s = Solution()
  print s.longestPalindromeSubseq('aabaa')

class Solution(object):
  def reverseStr(self, s, k):
    idx = 0
    s = list(s)
    n = len(s)
    while idx < n:
      i = idx
      j = min(i + k - 1, n - 1)
      while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
      idx += 2 * k
    return ''.join(s)

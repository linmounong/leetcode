class Solution(object):

  def findMaxLength(self, nums):
    l = [None for _ in xrange(2 * len(nums) + 1)]
    l[0] = -1
    ret = 0
    score = 0
    for i, num in enumerate(nums):
      score += 1 if num == 1 else -1
      if l[score] is None:
        l[score] = i
      else:
        ret = max(ret, i - l[score])
    return ret

class Solution(object):

  def checkSubarraySum(self, nums, k):
    if k == 0:
      zero = False
      for num in nums:
        if zero and num == 0:
          return True
        zero = num == 0
      return False
    k = abs(k)
    d = {0: -1}
    mod = 0
    for i, num in enumerate(nums):
      mod += num
      mod %= k
      if mod in d:
        if i - d[mod] > 1:
          return True
      else:
        d[mod] = i
    return False

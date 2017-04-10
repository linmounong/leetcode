class Solution(object):
  def find132pattern(self, nums):
    if len(nums) < 3:
      return False

    n = len(nums)
    nextgt = range(n)
    for i in reversed(range(n)):
            j = i + 1
            while j < n and nums[j] <= nums[i]:
                j = nextgt[j]
            nextgt[i] = j

    cap = None
    for i in reversed(range(n - 1)):
      num = nums[i]
      if cap is not None and num < cap:
        return True
      j = i + 1
      if (cap is None or num > cap) and num > nums[j]:
        while nextgt[j] < n and num > nums[nextgt[j]]:
          j = nextgt[j]
        cap = nums[j]
    return False

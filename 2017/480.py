import heapq

class MinHeap(object):
  sign = 1

  def __init__(self):
    self.l = []

  def push(self, n):
    heapq.heappush(self.l, self.sign * n)

  def pop(self):
    return self.sign * heapq.heappop(self.l)

  def peek(self):
    return self.sign * self.l[0]

class MaxHeap(MinHeap):
  sign = -1

class Solution(object):

  def medianSlidingWindow(self, nums, k):
    if k == 1:
      return [float(num) for num in nums]
    upper = MinHeap()
    lower = MaxHeap()
    for num in nums[:k]:
      upper.push(num)
    for _ in range(k / 2):
      lower.push(upper.pop())

    delcnt = {}

    def get_median():
      if k % 2:
        return float(upper.peek())
      return (upper.peek() + lower.peek()) / 2.0

    ret = [get_median()]
    i = k
    while i < len(nums):
      deleted = nums[i - k]
      added = nums[i]
      i += 1
      delcnt[deleted] = delcnt.get(deleted, 0) + 1
      if deleted >= upper.peek():
        upper.push(added)
      else:
        lower.push(added)
      if upper.peek() < lower.peek():
        lower.push(upper.pop())
        upper.push(lower.pop())
      while delcnt.get(upper.peek()):
        delcnt[upper.pop()] -= 1
      while delcnt.get(lower.peek()):
        delcnt[lower.pop()] -= 1
      ret.append(get_median())
    return ret

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print s.medianSlidingWindow(nums, k)
nums = [1,2]
k = 1
print s.medianSlidingWindow(nums, k)

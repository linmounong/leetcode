# Definition for an interval.
# class Interval(object):
#   def __init__(self, s=0, e=0):
#     self.start = s
#     self.end = e

class Solution(object):
  def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    n = len(intervals)
    if not n:
      return 0
    s = [i.start for i in intervals]
    e = [i.end for i in intervals]
    si = range(n)
    si.sort(cmp=lambda x, y: (s[x] - s[y]) or ((e[x] - s[x]) - (e[y] - s[y])))
    ei = range(n)
    ei.sort(cmp=lambda x, y: (e[x] - e[y]) or ((e[x] - s[x]) - (e[y] - s[y])))
    invalid = set()
    i = j = 0
    while i < n:
      if ei[i] not in invalid:
        while j < n and si[j] != ei[i]:
          invalid.add(si[j])
          j += 1
        if j < n:
          j += 1
      i += 1
    indices = [i for i in si if i not in invalid]
    n_chosen = 0
    end = s[indices[0]]
    for i in indices:
      if s[i] >= end:
        n_chosen += 1
        end = e[i]
    return n - n_chosen
#         
# class Interval(object):
#   def __init__(self, s=0, e=0):
#     self.start = s
#     self.end = e
# def foo(data):
#   return [Interval(s, e) for s, e in data]
# s = Solution()
# print s.eraseOverlapIntervals(foo([ [1,2], [2,3] ]))

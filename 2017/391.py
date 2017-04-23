import collections

class Solution(object):
  def isRectangleCover(self, rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: bool
    """
    xmin, ymin, xmax, ymax = rectangles[0]
    size = 0
    cnt = collections.Counter()
    for x0, y0, x1, y1 in rectangles:
      size += (x1 - x0) * (y1 - y0)
      cnt[(x0, y0)] += 1
      cnt[(x1, y0)] += 1
      cnt[(x1, y1)] += 1
      cnt[(x0, y1)] += 1
      if x0 < xmin:
        xmin = x0
      if x1 > xmax:
        xmax = x1
      if y0 < ymin:
        ymin = y0
      if y1 > ymax:
        ymax = y1
    if size != (xmax - xmin) * (ymax - ymin):
      return False
    corners = ((xmin, ymin), (xmax, ymin), (xmin, ymax), (xmax, ymax))
    if any(cnt[(x, y)] != 1 for x, y in corners):
      return False
    if any(cnt[(x, y)] %2 for x, y in cnt.iterkeys() if (x, y) not in corners):
      return False
    return True

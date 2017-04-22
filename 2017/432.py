class Node(object):
  def __init__(self, val=None):
    self.val = val
    self.left = None
    self.right = None
  
  def detach(self):
    left = self.left
    right = self.right
    left.right, right.left = right, left

  def inject_to(self, left):
    right = left.right
    left.right, right.left, self.left, self.right = self, self, left, right

class Bilink(object):
  def __init__(self):
    self.start = Node()
    self.end = Node()
    self.start.right = self.end
    self.end.left = self.start
  
  @property
  def empty(self):
    return self.start.right == self.end
  

class AllOne(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.link = Bilink()  # node: (count, keys)
    self.counts = {}  # key -> count
    self.nodes = {}  # key -> node

  def inc(self, key):
    """
    Inserts a new key <Key> with value 1. Or increments an existing key by 1.
    :type key: str
    :rtype: void
    """
    if key in self.counts:
      node = self.nodes[key]
      node.val[1].remove(key)
      self.counts[key] += 1
    else:
      node = self.link.start
      self.counts[key] = 1
    count = self.counts[key]
    if not node.right.val or node.right.val[0] != count:
      n = Node(val=(count, set()))
      n.inject_to(node)
    node = node.right
    self.nodes[key] = node
    node.val[1].add(key)

  def dec(self, key):
    """
    Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
    :type key: str
    :rtype: void
    """
    if key not in self.counts:
      return
    node = self.nodes[key]
    node.val[1].remove(key)
    count = self.counts[key] - 1
    if count == 0:
      del self.counts[key]
      del self.nodes[key]
    else:
      self.counts[key] = count
      if not node.left.val or node.left.val[0] != count:
        n = Node(val=(count, set()))
        n.inject_to(node.left)
      node = node.left
      self.nodes[key] = node
      node.val[1].add(key)


  def getMaxKey(self):
    """
    Returns one of the keys with maximal value.
    :rtype: str
    """
    while not self.link.empty and not self.link.end.left.val[1]:
      self.link.end.left.detach()
    if not self.link.empty:
      return next(iter(self.link.end.left.val[1]))
    return ''

  def getMinKey(self):
    """
    Returns one of the keys with Minimal value.
    :rtype: str
    """
    while not self.link.empty and not self.link.start.right.val[1]:
      self.link.start.right.detach()
    if not self.link.empty:
      return next(iter(self.link.start.right.val[1]))
    return ''

# obj = AllOne()
# obj.inc('a')
# obj.inc('b')
# obj.inc('b')
# obj.inc('b')
# obj.inc('b')
# obj.dec('b')
# obj.dec('b')
# print obj.getMaxKey()
# print obj.getMinKey()

class Node(object):
  def __init__(self):
    self.left = None
    self.right = None
    self.val = None
    self.key = None
    self.freq = 0

def detach(node):
  node.left.right, node.right.left = node.right, node.left
  return node.left.left is None and node.right.right is None

def inject(node, left):
  right = left.right
  left.right, right.left, node.left, node.right = node, node, left, right

def new_link():
  start, end = Node(), Node()
  start.right, end.left = end, start
  return start, end

def new_link_node(left):
  node = Node()
  inject(node, left)
  node.val = new_link()
  return node

class LFUCache(object):

  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.cap = capacity
    self.cache = {}  # key => val node
    self.freqs = {}  # n => freq node, node.val is a val link (start, end)
    self.freqstart, self.freqend = new_link()  # freq link (start, end)

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    if key not in self.cache:
      return -1
    node = self.cache[key]
    freq = self.freqs[node.freq]
    if detach(node):
      detach(freq)
      del self.freqs[node.freq]
    node.freq += 1
    if node.freq not in self.freqs:
      new_freq = new_link_node(freq.right.left)
      self.freqs[node.freq] = new_freq
    start = self.freqs[node.freq].val[0]
    inject(node, start)
    return node.val

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    if self.cap <= 0:
        return
    if len(self.cache) == self.cap and key not in self.cache:
      freq = self.freqstart.right
      node = freq.val[1].left
      if detach(node):
        detach(freq)
        del self.freqs[node.freq]
      del self.cache[node.key]
    if key not in self.cache:
      node = Node()
      node.val = value
      node.key = key
      self.cache[key] = node
      if 0 not in self.freqs:
        freq = new_link_node(self.freqstart)
        freq.freq = 0
        self.freqs[0] = freq
      inject(node, self.freqs[0].val[0])
    else:
      self.cache[key].val = value
    self.get(key)

# cache = LFUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print cache.get(1)  # returns 1
# cache.put(3, 3)     # evicts key 2
# print cache.get(2)  # returns -1 (not found)
# print cache.get(3)  # returns 3.
# cache.put(4, 4)     # evicts key 1.
# print cache.get(1)  # returns -1 (not found)
# print cache.get(3)  # returns 3
# print cache.get(4)  # returns 4

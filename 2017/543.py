# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def diameterOfBinaryTree(self, root):
    self.d = 0
    self.depth(root)
    return self.d

  def depth(self, root):
    if not root:
      return 0
    l = self.depth(root.left)
    r = self.depth(root.right)
    self.d = max(self.d, l + r)
    return max(l, r) + 1

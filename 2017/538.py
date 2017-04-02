# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        visit(root, 0)
        return root
    
def visit(root, base):
    if not root:
        return 0
    rsum = visit(root.right, base)
    lsum = visit(root.left, base + root.val + rsum)
    ret = root.val + lsum + rsum
    root.val += base + rsum
    return ret

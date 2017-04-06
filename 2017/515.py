# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        row = [root]
        while row:
            newrow = []
            tmp = None
            for node in row:
                if node.left:
                    newrow.append(node.left)
                if node.right:
                    newrow.append(node.right)
                if tmp is None or tmp < node.val:
                    tmp = node.val
            ret.append(tmp)
            row = newrow
        return ret

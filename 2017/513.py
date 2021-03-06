# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        row = [root]
        while row:
            ret = row[0].val
            newrow = []
            for node in row:
                if node.left:
                    newrow.append(node.left)
                if node.right:
                    newrow.append(node.right)
            row = newrow
        return ret

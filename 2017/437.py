# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        presum = collections.Counter({0: 1})
        ret = [0]
        def foo(node, cur):
            if not node:
                return
            cur += node.val
            ret[0] += presum[cur - sum]
            presum[cur] += 1
            foo(node.left, cur)
            foo(node.right, cur)
            presum[cur] -= 1
        foo(root, 0)
        return ret[0]

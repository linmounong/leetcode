# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cnt = {}
        def foo(node):
            if not node:
                return 0
            lsum = foo(node.left)
            rsum = foo(node.right)
            s = lsum + rsum + node.val
            cnt[s] = cnt.get(s, 0) + 1
            return s
        foo(root)
        maxsum = max(cnt.values())
        return [k for k, v in cnt.iteritems() if v == maxsum]

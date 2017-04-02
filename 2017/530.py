# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        state = [None, None]
        foo(root, state)
        return state[1]

def foo(node, state):
    if not node:
        return
    foo(node.left, state)
    if state[0] is None:
        state[0] = node.val
    else:
        diff = node.val - state[0]
        state[0] = node.val
        if state[1] is None:
            state[1] = diff
        else:
            state[1] = min(state[1], diff)
    foo(node.right, state)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        state = [None, 0, 0]  # current value, current count, max count
        def foo(node):
            if not node:
                return
            foo(node.left)
            if node.val != state[0]:
                state[0] = node.val
                state[1] = 0
            state[1] += 1
            if state[1] == state[2]:
                ret.append(state[0])
            elif state[1] > state[2]:
                del ret[:]
                ret.append(state[0])
                state[2] = state[1]
            foo(node.right)
        foo(root)
        return ret

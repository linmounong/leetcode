# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        start = last = TreeNode(key - 1)
        last.right = root
        node = root
        while node:
            if node.val < key:
                newnode = node.right
            elif node.val > key:
                newnode = node.left
            else:
                break
            last = node
            node = newnode
        else:
            return start.right
        if not node.left:
            replace(last, node, node.right)
            return start.right
        if not node.right:
            replace(last, node, node.left)
            return start.right
        if not node.left.right:
            node.left.right = node.right
            replace(last, node, node.left)
            return start.right
        i = node.left
        j = i.right
        while j.right:
            i = j
            j = j.right
        i.right = j.left
        j.left = node.left
        j.right = node.right
        replace(last, node, j)
        return start.right
            

def replace(parent, child, newchild):
    if parent.left == child:
        parent.left = newchild
    else:
        parent.right = newchild

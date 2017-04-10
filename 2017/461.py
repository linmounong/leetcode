class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        ret = 0
        while z:
            ret += z % 2
            z /= 2
        return ret

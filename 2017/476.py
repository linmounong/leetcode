class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        import math
        k = int(math.log(num, 2))
        return 2 ** (k + 1) - num - 1

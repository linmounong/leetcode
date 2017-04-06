class Solution(object):

    def convertToBase7(self, num):

        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = -num
            prefix = '-'
        else:
            prefix = ''
        tmp = []
        while num:
            tmp.append(str(num % 7))
            num //= 7
        return prefix + ''.join(reversed(tmp))

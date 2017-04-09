class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        s = [1, 2, 2]
        nextnum = 1
        cnt = 1
        i = 2
        while i < n:
            if s[i] == 1:
                cnt += 1
                s.append(nextnum)
            else:
                s.append(nextnum)
                s.append(nextnum)
            nextnum = 3 - nextnum
            i += 1
        return cnt

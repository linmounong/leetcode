class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n / 2 + 1):
            if n % i:
                continue
            k = n / i
            if s == s[:i] * k:
                return True
        return False

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        t = []
        for c in reversed(S):
            if c == '-':
                continue
            if len(t) % (K + 1) == 0:
                t.append('-')
            t.append(c.upper())
        return ''.join(reversed(t[1:]))

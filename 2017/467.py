class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        p = [ord(c) - ord('a') for c in p]
        cap = [0 for _ in range(26)]
        i = 0
        while i < n:
            j = i + 1
            while j < n and (p[j] - p[j - 1]) % 26 == 1:
                j += 1
            while i < j:
                cap[p[i]] = max(cap[p[i]], j - i)
                i += 1
        return sum(cap)

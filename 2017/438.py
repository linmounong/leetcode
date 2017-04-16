import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        if len(s) < n:
            return []
        cnt = collections.Counter(p)
        tomatch = n
        for c in s[:n]:
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] >= 0:
                    tomatch -= 1
        if tomatch == 0:
            ret = [0]
        else:
            ret = []
        i = 1
        for i in range(0, len(s) - n):
            removed = s[i]
            if removed in cnt:
                cnt[removed] += 1
                if cnt[removed] > 0:
                    tomatch += 1
            added = s[i + n]
            if added in cnt:
                cnt[added] -= 1
                if cnt[added] >= 0:
                    tomatch -= 1
                    if tomatch == 0:
                        ret.append(i + 1)
            i += 1
        return ret

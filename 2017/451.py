import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        revcnt = {}
        for c, cnt in counter.iteritems():
            if cnt not in revcnt:
                revcnt[cnt] = set()
            revcnt[cnt].add(c)
        return ''.join(c * cnt for cnt in sorted(revcnt.keys(), reverse=True) for c in revcnt[cnt])

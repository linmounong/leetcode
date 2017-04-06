class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        patterns = [compile(s) for s in strs]
        n = len(strs)
        ret = -1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if is_subsequence(strs[i], patterns[j]):
                    break
            else:
                ret = max(ret, len(strs[i]))
        return ret

def compile(s):
    pattern = []
    tmp = {}
    for i in reversed(range(len(s))):
        pattern.append(dict(tmp))
        tmp[s[i]] = i + 1
    pattern.append(tmp)
    pattern.reverse()
    return pattern

def is_subsequence(s, pattern):
    i = 0
    for c in s:
        if c not in pattern[i]:
            return False
        i = pattern[i][c]
    return True

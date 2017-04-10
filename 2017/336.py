class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        info = [(w[::-1], True, i) for i, w in enumerate(words)]
        info.extend((w, False, i) for i, w in enumerate(words))
        info.sort(cmp=lambda x, y: len(x) - len(y) if len(x) != len(y) else -1 if x < y else 1)
        i = 0
        n = len(info)
        pairs = []
        while i < n:
            w, r, idx = info[i]
            j = i + 1
            while j < n:
                w2, r2, idx2 = info[j]
                j += 1
                if idx == idx2:
                    continue
                if not w2.startswith(w):
                    break
                if not r ^ r2:
                    continue
                sub = w2[len(w):]
                if sub == sub[::-1]:
                    if r:
                        pairs.append([idx2, idx])
                    else:
                        pairs.append([idx, idx2])
            i += 1
        return pairs

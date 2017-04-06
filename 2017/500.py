class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [w for w in words if isvalid(w)]

def isvalid(word):
    group = None
    for c in word.lower():
        if group is None:
            group = groupof(c)
        elif group != groupof(c):
            return False
    return True

def groupof(c):
    if c in 'zxcvbnm':
        return 1
    if c in 'asdfghjkl':
        return 2
    return 3

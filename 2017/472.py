class Solution(object):
  def findAllConcatenatedWordsInADict(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    s = set()
    def foo(word):
      if not s:
        return False
      n = len(word)
      dp = [False] * (n + 1)
      dp[0] = True
      for i in range(1, n + 1):
        for j in range(i):
          if not dp[j]:
            continue
          if word[j:i] in s:
            dp[i] = True
            break
      return dp[n]
    ret = []
    for word in words:
      if foo(word):
        ret.append(word)
      s.add(word)
    return ret

# s = Solution()
# with open('472.txt') as df:
#   words = [w.strip('[]"') for w in df.read().split(',')]
# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# print len(words)
# print s.findAllConcatenatedWordsInADict(words)

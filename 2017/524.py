class Solution(object):
  def findLongestWord(self, s, d):
    nextchar = []
    tmp = {}
    for i in range(len(s) - 1, -1, -1):
      c = s[i]
      nextchar.append(dict(tmp))
      tmp[c] = i + 1
    nextchar.append(tmp)
    nextchar.reverse()
    ret = ''
    for word in d:
      if (len(word) > len(ret) or (len(word) == len(ret) and word < ret)) and foo(word, nextchar):
        ret = word
    return ret

def foo(word, nextchar):
  i = 0
  for c in word:
    if c not in nextchar[i]:
      return False
    i = nextchar[i][c]
  return True

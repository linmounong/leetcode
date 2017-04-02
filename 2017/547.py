class Solution(object):

  def findCircleNum(self, M):
    N = len(M)
    heads = {i: i for i in range(N)}
    for i in range(N):
      for j in range(0, i):
        if M[i][j]:
          merge(heads, i, j)
    groups = set()
    for i in heads:
      while i != heads[i]:
        i = heads[i]
      groups.add(i)
    return len(groups)

def merge(heads, i, j):
  while heads[i] != heads[heads[i]]:
    heads[i] = heads[heads[i]]
  while heads[j] != heads[heads[j]]:
    heads[j] = heads[heads[j]]
  heads[heads[i]] = heads[j]

# s = Solution()
# input = [[1,1,0],
#          [1,1,0],
#          [0,0,1]]
# print s.findCircleNum(input)
# input = [[1,1,0],
#          [1,1,1],
#          [0,1,1]]
# print s.findCircleNum(input)

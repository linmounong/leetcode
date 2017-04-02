class Solution(object):

  def updateMatrix(self, matrix):
    q = []
    for i, row in enumerate(matrix):
      for j, val in enumerate(row):
        if val == 0:
          q.append((i, j))
    while q:
      q2 = []
      for i, j in q:
        val = matrix[i][j] - 1
        foo(matrix, i+1, j, val, q2)
        foo(matrix, i-1, j, val, q2)
        foo(matrix, i, j+1, val, q2)
        foo(matrix, i, j-1, val, q2)
      q = q2
    for row in matrix:
      for j, val in enumerate(row):
        row[j] = -val
    return matrix

def foo(matrix, i, j, val, q):
  if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] > 0:
    matrix[i][j] = val
    q.append((i, j))

# s = Solution()
# input = [[0, 0, 0],
#          [0, 1, 0],
#          [0, 0, 0]]
# print s.updateMatrix(input)
# input = [[0, 0, 0],
#          [0, 1, 0],
#          [1, 1, 1]]
# print s.updateMatrix(input)

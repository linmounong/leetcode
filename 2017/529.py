class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        n = len(board)
        m = len(board[0])
        dij = ((-1, -1), (-1, 0), (-1, 1),
               ( 0, -1),          ( 0, 1),
               ( 1, -1), ( 1, 0), ( 1, 1))
        def count_adjacent_mines(i, j):
            ret = 0
            for di, dj in dij:
                if 0 <= i+di < n and 0 <= j+dj < m and board[i+di][j+dj] == 'M':
                    ret += 1
            return ret
        def reveal(i, j):
            if not (0 <= i < n and 0 <= j < m and board[i][j] == 'E'):
                return
            cnt= count_adjacent_mines(i, j)
            if cnt > 0:
                board[i][j] = str(cnt)
                return
            board[i][j] = 'B'
            for di, dj in dij:
                reveal(i+di, j+dj)
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            reveal(i, j)
        return board

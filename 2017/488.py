class Solution(object):

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        t = []  # list of [ball, count]
        for ball in board:
            if not t or t[-1][0] != ball:
                t.append([ball, 0])
            t[-1][1] += 1
        board = t
        t = {}
        for ball in hand:
            t[ball] = t.get(ball, 0) + 1
        hand = t
        ret = [6]

        def foo(cnt, board):
            if cnt >= ret[0]:
                return
            if not board:
                ret[0] = min(ret[0], cnt)
                return
            for ball in hand:
                if not hand[ball]:
                    continue
                hand[ball] -= 1
                for i, seg in enumerate(board):
                    if seg[0] == ball:
                        foo(cnt + 1, blow(board, i))
                hand[ball] += 1

        def blow(board, i):
            board = [list(seg) for seg in board]  # deep copy
            board[i][1] += 1
            while 0 <= i < len(board) and board[i][1] >= 3:
                del board[i]
                i -= 1
                if 0 <= i < len(board) - 1 and board[i][0] == board[i + 1][0]:
                    board[i][1] += board[i + 1][1]
                    del board[i + 1]
            return board

        foo(0, board)
        return ret[0] if ret[0] < 6 else -1

# s = Solution()
# board = "WWRRBBWW"
# hand = "WRBRW"
# print s.findMinStep(board, hand)

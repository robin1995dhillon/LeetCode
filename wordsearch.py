class Solution(object):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def exist(self, board, word):
        if (len(word) == 0):
            return True
        n = len(board)
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if (word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
        return False

    def solution(self, board, word, x, y, curString):
        if (x < 0 or x >= len(board) or y < 0 or y >= len(board[x] or board[x][y] == ' ')):
            return False
        curString += board[x][y]
        if (len(curString) > len(word)):
            return False
        if (curString[len(curString) - 1] != word[len(curString) - 1]):
            return False
        if (curString == word):
            return True

        temp = board[x][y]
        board[x][y] = ' '
        for i in range(4):
            if (self.solution(board, word, x + self.dx[i], y + self.dy[i], curString)):
                return True

        board[x][y] = temp
        return False

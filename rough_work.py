class Solution(object):
    def exist(self, board, word):
        if len(word) == 0:
            return True
        cur=""
        rows = len(board)
        columns = len(board[0])
        value = self.dfs(board,word,rows,columns,cur)
        return value
    def dfs(self,board,word,rows,columns,cur):
        for r in range(0,rows):
            for c in range(0,columns):
                if r>=rows or c>=columns or len(cur)>word:
                    return False
                if board[r][c]==




















s = Solution()
board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"
value = s.exist(board,word)
print(value)
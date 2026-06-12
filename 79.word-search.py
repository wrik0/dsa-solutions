#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-08 18:58
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def match(board, cell, s):
            i , j = cell
            if len(s) == 1 and board[i][j] == s: return True
            if board[i][j] != s[0]: return False
            s = s[1:]
            m, n = len(board), len(board[0])
            val = board[i][j]
            board[i][j] = "."
            m_right = m_left = m_top = m_bot = False
            #move right
            if j < n - 1 and board[i][j + 1] != ".":
                m_right = match(board, [i, j + 1], s)
            #move left
            if j > 0 and board[i][j - 1] != ".":
                m_left = match(board, [i, j - 1], s)
            #move top
            if i > 0 and board[i - 1][j] != ".":
                m_top = match(board, [i - 1, j], s)
            #move bottom
            if i < m - 1 and board[i + 1][j] != ".":
                m_bot = match(board, [i + 1, j], s)
            
            board[i][j] = val

            return m_right or m_left or m_top or m_bot

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if match(board, [i,j], word): return True
        
        return False

# @lc code=end

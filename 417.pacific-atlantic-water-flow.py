#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-08 20:41
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacificBeach = [[i, 0] for i in range(m)] + [[0, j] for j in range(n)]
        atlanticBeach = [[i, n-1] for i in range(m)] + [[m-1, j] for j in range(n)]

        self.ptal = set()
        self.atal = set()
        def help(cell, tally):
            if cell in tally: return
            tally.add(cell)
            i, j = cell
            # check down
            if i < m - 1 and heights[i + 1][j] >= heights[i][j]:
                help(tuple([i+1, j]), tally)
            # check right
            if j < n - 1 and heights[i][j+1] >= heights[i][j]:
                help(tuple([i, j+1]), tally)
             # check up
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                help(tuple([i-1, j]), tally)
            # check left
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                help(tuple([i, j-1]), tally)

        for i, j in pacificBeach:
            help(tuple([i,j]), self.ptal)

        for i, j in atlanticBeach:
            help(tuple([i,j]), self.atal)

        if len(self.ptal) < len(self.atal):
            self.ptal, self.atal = self.atal, self.ptal

        res = []
        for cell in self.ptal:
            if cell in self.ptal and cell in self.atal:
                i, j = cell
                res.append([i,j])

        return res

# @lc code=end

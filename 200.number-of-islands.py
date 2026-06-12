#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-02 17:18
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.traverse(grid, i, j)
        return res

    def traverse(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        grid[i][j] = "0"
        # traverse left
        if j > 0 and grid[i ][j - 1] == "1":
            self.traverse(grid, i , j -1)
        # traverse right
        if j < n - 1 and grid[i][j + 1] == "1":
            self.traverse(grid, i, j + 1)
        # traverse top
        if i > 0 and grid[i - 1][j] == "1":
            self.traverse(grid, i - 1, j)
        # traverse bottom
        if i < m - 1 and grid[i + 1][j] == "1":
            self.traverse(grid, i + 1, j)

# @lc code=end

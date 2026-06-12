#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-15 17:36
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

# @lc code=end

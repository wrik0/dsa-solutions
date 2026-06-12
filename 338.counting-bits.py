#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-28 12:07
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i] = (1 & i) + dp[i >> 1]

        return dp

# @lc code=end

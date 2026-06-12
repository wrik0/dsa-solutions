#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-28 12:14
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n > 0:
            n = n & (n - 1)
            c += 1
        return c

# @lc code=end

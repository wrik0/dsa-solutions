#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 14:07
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = s = 0

        for i in range(k):
            s += nums[i]
        res = s

        for r in range(k, len(nums)):
            s += nums[r]
            s -= nums [l]
            l += 1
            res = max(s, res)

        return res/k

# @lc code=end

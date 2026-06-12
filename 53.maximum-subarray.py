#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-09 21:07
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = float("-inf")
        currSum = 0

        for num in nums:
            currSum = max(num, currSum + num)
            bestSum = max(bestSum, currSum)

        return bestSum

# @lc code=end

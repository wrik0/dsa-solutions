#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-22 22:10
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prevPrice = prices[0]
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prevPrice) 
            prevPrice = prices[i]
        
        return profit

# @lc code=end

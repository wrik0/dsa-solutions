#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_hold = -prices[0]
        prev_free = prev_cooldown = 0

        for i in range(1, len(prices)):
            hold = max(prev_hold, prev_free - prices[i])
            free = max(prev_free, prev_cooldown)
            cooldown = prev_hold + prices[i]

            prev_hold, prev_free, prev_cooldown = hold, free, cooldown

        return max(prev_cooldown, prev_free)


# @lc code=end

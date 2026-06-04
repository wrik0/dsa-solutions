#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            if rem in memo:
                return memo[rem]

            min_count = float("inf")

            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_count = min(min_count, res + 1)

            memo[rem] = -1 if min_count == float("inf") else min_count
            return memo[rem]

        return dfs(amount)


# @lc code=end

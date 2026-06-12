#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-30 22:36
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

# @lc code=end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-07 21:26
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def helper(curr, idx, s):
            if s > target: return
            if s == target: self.res.append(curr[:])
            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                helper(curr, i, s + candidates[i])
                curr.pop()
        helper([], 0, 0)
        return self.res

# @lc code=end

#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-06 20:57
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def helper(curr, idx):
            self.res.append(curr[:])
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                helper(curr, i + 1)
                curr.pop()
        helper([], 0)
        return self.res

# @lc code=end

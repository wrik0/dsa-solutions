#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-07 20:54
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        def helper(curr, idx):
            self.res.append(curr[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]: continue
                curr.append(nums[i])
                helper(curr, i + 1)
                curr.pop()
        helper([], 0)
        return self.res

# @lc code=end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-07 21:11
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def helper(curr):
            if len(curr) == len(nums): self.res.append(curr[:])
            for i in range(len(nums)):
                if nums[i] in curr: continue 
                curr.append(nums[i])
                helper(curr)
                curr.pop()
        helper([])
        return self.res

# @lc code=end

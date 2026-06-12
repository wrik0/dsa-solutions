#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-07 22:02
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        def helper(curr):
            if len(curr) == len(nums):
                self.res.append([nums[i] for i in curr])
            for i in range(len(nums)):
                if i in curr: continue
                if i > 0 and i-1 not in curr and nums[i] == nums[i - 1]:
                    continue
                curr.append(i)
                helper(curr)
                curr.pop()

        helper([])
        return self.res

# @lc code=end

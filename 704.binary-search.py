#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 19:53
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target: return m
            if nums[m] < target: l = m + 1
            else: r = m - 1
            
        return -1

# @lc code=end

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-02 17:35
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        low = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                low = m
                r = m - 1

        l, r = 0, len(nums) - 1
        high = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                high = m
                l = m + 1

        return [low, high]

# @lc code=end

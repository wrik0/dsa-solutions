#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 17:50
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            hl, hr = height[l], height[r]
            area = max(area , (r-l) * min(hl, hr))

            if hl >= hr: r -= 1
            else: l += 1

        return area

# @lc code=end

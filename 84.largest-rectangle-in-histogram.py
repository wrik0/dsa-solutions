#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-31 14:35
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                left_height_idx, height = stack.pop()
                width = i - left_height_idx
                max_area = max(max_area, width * height)
                index = left_height_idx
            stack.append([index, h])

        for idx, height in stack:
            h_max_idx = len(heights) - 1
            width = h_max_idx - idx + 1
            max_area = max(width * height, max_area)
        
        return max_area

# @lc code=end

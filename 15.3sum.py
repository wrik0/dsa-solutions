#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 18:43
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        arr = sorted(nums)
        if arr[0] > 0: return res
        for idx in range(len(arr)):
            if idx > 0 and arr[idx] == arr[idx - 1]: continue 
            target = 0 - arr[idx]
            l, r = idx + 1, len(arr) - 1
            while l < r:
                if arr[l] + arr[r] == target:
                    res.append([arr[idx], arr[l], arr[r]])
                    while l < len(arr) -1 and arr[l] == arr [l+1]: l += 1
                    while r> l+ 1 and arr[r] == arr [r -1]: r -= 1
                    r, l = r-1, l+1
                elif arr[l] + arr[r] > target: 
                    r -= 1
                elif arr[l] + arr[r] < target: 
                    l += 1
        
        return res

# @lc code=end

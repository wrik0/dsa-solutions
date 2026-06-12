#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-22 16:20
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l ) // 2

            if nums[m] == target: return m
            
            # now there are two possibilities
            # m is in the broken segement of the array, ie. break lies in [m,r]
            if nums[m] > nums[r]:
                # now also there are two possibilites, does the solution lie between
                # l and m, i.e. the sorted section? 
                if nums[l] <= target and nums[m] >= target:
                    r = m - 1
                # target lies in the unsorted section i.e between m and r
                else:   
                    l = m + 1
            # m is in the sorted segment of the array i.e. break lies in [l, m]
            else:
                # target lies in  the sorted part [m, r]
                if nums[m] <= target and nums[r] >= target:
                    l = m + 1
                #target lies in the unsorted part, i.e the one with the break
                else:
                    r = m - 1
        
        return -1

# @lc code=end

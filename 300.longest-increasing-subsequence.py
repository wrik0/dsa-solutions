#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# TODO: revisit concept
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = [nums[0]]

        def search(piles: List[int], target: int) -> int:
            """
            bisesct function takes in a searchable piles
            array and a target as a parameter

            if an element is found in the pile which is greater
            than the element, it returns the index of the same
            while searching for a smaller element
            if not it returns -1
            """
            el = -1
            l, r = 0, len(piles) - 1
            while l <= r:
                m = l + (r - l) // 2
                if piles[m] >= target:
                    el = m
                    r = m - 1
                else:
                    l = m + 1

            return el

        for i in range(1, len(nums)):
            res = search(piles, nums[i])
            if res < 0:
                piles.append(nums[i])
            else:
                piles[res] = nums[i]

        # length of piles acts like a length ledger 
        # for maintaining size of LIS, not state of
        # record IMPORTANT 
        return len(piles) 

        
# @lc code=end


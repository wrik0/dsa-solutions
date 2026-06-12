#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-22 16:51
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles) / h)
        r = max(piles)
        def eatingTime(k) -> int:
            nonlocal piles, h
            t = 0
            for pile in piles:
                # note: this will not give correct value, but will early exit
                # this suffices since we do not need exact count, just the info
                # if Koko can have the bananas in time
                if t > h: return t
                if pile < k: 
                    t += 1
                else:
                    t += (pile + k - 1) // k
            return t

        while l <= r: 
            m = l + (r - l)// 2
            if eatingTime(m) <= h:
                r = m - 1
            else: 
                l = m + 1

        return l

# @lc code=end

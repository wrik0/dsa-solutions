#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 14:43
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res= 0
        max_freq, tally = 0, dict()

        for r in range(len(s)):
            tally[s[r]] = tally.get(s[r], 0) + 1
            max_freq = max(max_freq, tally[s[r]])
            if (r - l + 1) - max_freq > k: 
                tally[s[l]] -= 1
                l += 1
        
        return r-l+1

# @lc code=end

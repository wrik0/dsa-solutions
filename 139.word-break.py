#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-05-22 21:50
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True 
        wordSet = set(wordDict)
        minWord = min([len(word) for word in wordDict])
        maxWord = max([len(word) for word in wordDict])

        for i in range(minWord, len(s) + 1):
            for j in range(max(i - maxWord, 0), i):
                dp[i] = (s[j:i] in wordSet and dp[j]) or dp[i]
            
        return dp[-1]

# @lc code=end

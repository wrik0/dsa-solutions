#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp_prev = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            dp = [0] * (len(text2) + 1)
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp_prev[j - 1] + 1
                else:
                    dp[j] = max(
                        dp[j - 1],
                        dp_prev[j],
                    )
            dp_prev = dp

        return dp_prev[len(text2)]

    # NO SPACE OPTIMIZATION VERSION
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     dp = [[0 for _ in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    #     for i in range(1, len(text1) + 1):
    #         for j in range(1, len(text2) + 1):
    #             if text1[i - 1] == text2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1] + 1
    #             else:
    #                 dp[i][j] = max(
    #                     dp[i - 1][j],  # lcs count till the first string
    #                     dp[i][j - 1],  # lcs count till the second string
    #                 )

    #     return dp[-1][-1]


# @lc code=end

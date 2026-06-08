#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        dp_prev = [j for j in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            dp = [0] * (len(word2) + 1)
            dp[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = dp_prev[j - 1]
                else:
                    dp[j] = 1 + min(
                        dp_prev[j - 1],  # replacement
                        dp_prev[j],  # deletion
                        dp[j - 1],  # insertion
                    )
            dp_prev = dp

        return dp_prev[len(word2)]

    # NO SPACE OPTIMIZATION
    # def minDistance(self, word1: str, word2: str) -> int:
    #     dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    #     for j in range(len(word2) + 1):
    #         dp[0][j] = j
    #     for i in range(len(word1) + 1):
    #         dp[i][0] = i

    #     for i in range(1, len(word1) + 1):
    #         for j in range(1, len(word2) + 1):
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1]
    #             else:
    #                 dp[i][j] = 1 + min(
    #                     dp[i - 1][j - 1],  # replacement
    #                     dp[i - 1][j],  # deletion
    #                     dp[i][j - 1],  # insertion
    #                 )

    #     return dp[-1][-1]


# @lc code=end

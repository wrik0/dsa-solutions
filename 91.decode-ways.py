#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s[0] == "0" else 1
        prev = 0 if s[0] == "0" else 1
        curr = 0
        if s[1] != "0":
            curr += prev
        if 10 <= int(s[0:2]) <= 26:
            curr += prev

        for i in range(2, len(s)):
            tmp = 0
            if s[i] != "0":
                tmp += curr
            two_digit = s[i - 1 : i + 1]
            if 10 <= int(two_digit) <= 26:
                tmp += prev
            prev, curr = curr, tmp
        return curr


# @lc code=end

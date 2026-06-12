#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-21 13:58
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        N, a1, a2 = len(s1), self.alphArr(s1), [0] * 26

        # build initial window
        for i in range(N):
            a2[ord(s2[i]) - ord('a')] += 1

        # count initial matches
        matches = sum(1 for i in range(26) if a1[i] == a2[i])

        if matches == 26: return True

        # slide the window
        for r in range(N, len(s2)):
            # incoming character
            inc = ord(s2[r]) - ord('a')
            if a2[inc] == a1[inc]: matches -= 1  # was matching, about to change
            a2[inc] += 1
            if a2[inc] == a1[inc]: matches += 1  # check if matches now

            # outgoing character
            out = ord(s2[r - N]) - ord('a')
            if a2[out] == a1[out]: matches -= 1  # was matching, about to change
            a2[out] -= 1
            if a2[out] == a1[out]: matches += 1  # check if matches now

            if matches == 26: return True

        return False
            
    def alphArr(self, s: str) -> List:
        arr = [0] * 26
        start_ord = ord('a')
        for c in s:
            char_idx = ord(c) - start_ord
            arr[char_idx] += 1
        return arr

# @lc code=end

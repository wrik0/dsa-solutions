#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-25 12:51
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSumVal = -1001
       
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxPathSumVal
            if not node: return 0
            
            leftval = max(0,dfs(node.left))
            rightval = max(0, dfs(node.right))
            
            maxPathSumVal = max(maxPathSumVal, node.val + leftval + rightval)

            return node.val + max(leftval, rightval)

        dfs(root)

        return maxPathSumVal

# @lc code=end

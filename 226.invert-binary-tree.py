#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-31 19:01
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)
        return root

# @lc code=end

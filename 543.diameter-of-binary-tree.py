#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-31 21:27
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = {}
        stack = [root]
        dia = 0
        while stack:
            node = stack[-1]
            if not node:
                stack.pop()
                continue
            if node.right and node.right not in depth:
                stack.append(node.right)
                continue
            if node.left and node.left not in depth:
                stack.append(node.left)
                continue
            node = stack.pop()
            leftDepth = rightDepth = 0
            if node.left:
                leftDepth = depth[node.left] + 1
            if node.right:
                rightDepth = depth[node.right] + 1
            depth[node] = max(leftDepth, rightDepth)
            dia = max(dia, leftDepth + rightDepth)
        return dia

# @lc code=end

#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-02 10:39
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q: return True
            if p and q and p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                return True
            else: return False 
        if not subRoot: return True
        if not root and subRoot: return False
        if root.val == subRoot.val and isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# @lc code=end

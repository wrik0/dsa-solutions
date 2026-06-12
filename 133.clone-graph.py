#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-08 19:48
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.tally = {}
        def helper(node):
            if not node: return None
            if node.val in self.tally: return self.tally[node.val]
            clone = Node(
                node.val, 
                )
            self.tally[node.val] = clone
            clone.neighbors = [helper(x) for x in node.neighbors]
            return clone

        return helper(node)

# @lc code=end

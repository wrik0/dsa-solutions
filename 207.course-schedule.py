#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-09 20:42
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tally = {}
        for a, b in prerequisites:
            tally[b] = tally.get(b, set())
            tally[b].add(a)

        def dfs(node, visiting, visited):
            if node in visiting: return False
            if node in visited: return True
            visiting.add(node)
            for neighbor in tally.get(node, []):
                if not dfs(neighbor, visiting, visited): return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        visiting, visited = set(), set()
        for node in tally.keys():
            if not dfs(node, visiting, visited): return False
        
        return True

# @lc code=end

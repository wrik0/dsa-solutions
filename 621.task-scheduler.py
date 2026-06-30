#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from typing import List
import collections
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task Tally initialization
        taskMap = collections.defaultdict(int)
        for task in tasks:
            taskMap[task] += 1
        # heap population
        heap = []
        for task, effort in taskMap.items():
            # negating since Python default is min heap
            # and I need a max heap
            heapq.heappush(heap, (-effort, task))
        
        res = 0
        while heap:
            stack = []
            count = 0
            for i in range(n + 1):
                if not heap: break
                count += 1
                effort, task = heapq.heappop(heap)
                effort += 1
                if effort < 0:
                    stack.append((effort, task))

            for item in stack:
                heapq.heappush(heap, item)

            if heap:
                res += n +1
            else: 
                res += count

        return res
    
# @lc code=end

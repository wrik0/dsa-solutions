#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-04-06 19:59
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left: 
            heapq.heappush(self.left, -num)
            return
        liesToRight = num > -self.left[0]
        if liesToRight: heapq.heappush(self.right, num)
        else: heapq.heappush(self.left, -num)
        # now equalize
        while len(self.left) - len(self.right) > 1:
            el = -heapq.heappop(self.left)
            heapq.heappush(self.right, el)
        while len(self.right) > len(self.left) : 
            el = heapq.heappop(self.right)
            heapq.heappush(self.left, -el)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

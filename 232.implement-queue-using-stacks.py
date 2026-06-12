#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-30 21:53
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.pushkar = []
        self.pullkar = []

    def push(self, x: int) -> None:
        self.pushkar.append(x)

    def pop(self) -> int:
        if self.pullkar: return self.pullkar.pop()
        while self.pushkar:
            self.pullkar.append(self.pushkar[-1])
            self.pushkar.pop()
        return self.pullkar.pop()

    def peek(self) -> int:
        if self.pullkar: return self.pullkar[-1]
        return self.pushkar[0] 

    def empty(self) -> bool:
        return len(self.pushkar) == 0 and len(self.pullkar) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# @lc code=end

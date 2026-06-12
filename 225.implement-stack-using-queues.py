#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-30 22:21
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.q1 = collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def cycle_till_second_last(self) -> None:
        for i in range(len(self.q1) - 1):
            self.q1.append(self.q1.popleft())

    def pop(self) -> int:
        self.cycle_till_second_last()
        return self.q1.popleft()

    def top(self) -> int:
        self.cycle_till_second_last()
        el = self.q1.popleft()
        self.q1.append(el)
        return el

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# @lc code=end

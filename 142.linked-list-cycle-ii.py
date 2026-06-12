#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-20 14:05
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# @lc code=end

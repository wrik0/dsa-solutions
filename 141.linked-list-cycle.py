#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-20 13:53
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

# @lc code=end

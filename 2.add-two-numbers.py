#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Backup fetched on: 2026-06-12 21:03:36
# Solved on: 2026-03-20 16:28
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, digit = divmod(v1 + v2 + carry, 10)
            cur.next = cur = ListNode(digit)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# @lc code=end

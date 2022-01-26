# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow




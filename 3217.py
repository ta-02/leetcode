from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        curr = head
        new_head = curr
        nums_set = set(map(int, nums))

        while curr:
            if curr.val in nums_set:
                if new_head == curr:
                    new_head = curr.next
                curr = curr.next
                if prev:
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return new_head

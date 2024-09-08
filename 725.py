from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        res = []

        per = count // k
        div = count % k

        curr = head

        for _ in range(k):
            part_head = curr
            size = per + (1 if div > 0 else 0)
            div -= 1

            for _ in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

            res.append(part_head)

        return res

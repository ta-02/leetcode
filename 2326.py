from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(
        self,
        m: int,
        n: int,
        node: Optional[ListNode],
    ) -> List[List[int]]:
        t, b = 0, m - 1
        l, r = 0, n - 1
        res = [[-1] * n for _ in range(m)]

        while node:
            for i in range(l, r + 1):
                if not node:
                    return res
                res[t][i] = node.val
                node = node.next
            t += 1

            for i in range(t, b + 1):
                if not node:
                    return res
                res[i][r] = node.val
                node = node.next
            r -= 1

            for i in range(r, l - 1, -1):
                if not node:
                    return res
                res[b][i] = node.val
                node = node.next
            b -= 1

            for i in range(b, t - 1, -1):
                if not node:
                    return res
                res[i][l] = node.val
                node = node.next
            l += 1

        return res

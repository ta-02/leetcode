from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        return 0

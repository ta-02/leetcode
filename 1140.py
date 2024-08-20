from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        INF = 2**100

        @cache
        def dp(i, m, p):
            res = 0 if p == 0 or i >= N else INF
            acc = 0
            for j in range(i, min(N, i + 2 * m)):
                x = dp(j + 1, max(m, j - i + 1), p ^ 1)
                acc += piles[j]
                res = max(res, x + acc) if p == 0 else min(res, x)
            return res

        return dp(0, 1, 0)


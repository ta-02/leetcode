from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        INF = 2**10

        @cache
        def dfs(curr: int, copy: int) -> int:
            if curr == n:
                return 0
            if curr > n:
                return INF
            return 1 + min(
                dfs(curr + copy, copy),
                1 + dfs(curr + curr, curr),
            )

        return 1 + dfs(1, 1)

from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        row = defaultdict(list)
        col = defaultdict(list)
        for x, y in stones:
            row[x].append((x, y))
            col[y].append((x, y))

        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for u, v in row[x] + col[y]:
                dfs(u, v)

        r = 0
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                r += 1

        return n - r

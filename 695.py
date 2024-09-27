from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(x, y):
            a = 0
            if not (0 <= x < n and 0 <= y < m and grid[x][y] == 1):
                return a
            a += 1
            grid[x][y] = 0
            for x1, y1 in d:
                a += dfs(x + x1, y + y1)
            return a

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(dfs(i, j), res)
        return res

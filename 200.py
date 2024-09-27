from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and grid[x][y] == "1"):
                return
            grid[x][y] = "0"
            [dfs(x + dx, y + dy) for dx, dy in d]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res

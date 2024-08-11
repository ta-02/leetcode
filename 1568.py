from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(r: int, c: int, visited: set):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            for i, j in directions:
                dfs(r + i, c + j, visited)

        def count_islands():
            visited = set()
            count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c, visited)
                        count += 1
            return count

        if count_islands() != 1:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1
        return 2

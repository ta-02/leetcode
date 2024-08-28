from typing import List


class Solution:
    def countSubIslands(
        self,
        grid1: List[List[int]],
        grid2: List[List[int]],
    ) -> int:

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        R, C = len(grid1), len(grid1[0])
        res = 0

        def dfs(r, c) -> bool:
            if r < 0 or r >= R or c < 0 or c >= C or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0
            is_sub_island = grid1[r][c] == 1
            for i, j in dir:
                is_sub_island &= dfs(r + i, c + j)
            return is_sub_island

        for r in range(R):
            for c in range(C):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        res += 1

        return res

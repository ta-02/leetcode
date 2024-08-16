from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        isFound = False
        visited = set()

        def dfs(r: int, c: int, idx: int) -> None:
            nonlocal isFound
            if idx == len(word):
                isFound = True
                return

            if (
                r < 0
                or r >= R
                or c < 0
                or c >= C
                or board[r][c] != word[idx]
                or (r, c) in visited
            ):
                return

            visited.add((r, c))

            for i, j in directions:
                dfs(r + i, c + j, idx + 1)

            visited.remove((r, c))

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    dfs(r, c, 0)
                    if isFound:
                        return True

        return isFound

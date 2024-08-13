from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(idx: int, path: List[int], curr: int):
            if curr > target:
                return

            if curr == target:
                res.append(path)
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], curr + candidates[i])

        dfs(0, [], 0)
        return res

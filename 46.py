from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                res.append(path)
                return

            for i in range(N):
                dfs(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])

        dfs([], nums)
        return res

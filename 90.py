from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        n = len(nums)
        nums.sort()

        def dfs(i):
            if i >= n:
                res.add(tuple(subset[:]))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return list(res)

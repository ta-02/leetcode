from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res, p = [], []
        ans = 0
        for n in arr:
            ans ^= n
            p.append(ans)

        for l, r in queries:
            res.append(p[l - 1] ^ p[r] if l - 1 >= 0 else p[r])

        return res

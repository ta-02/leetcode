from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        low, high = arrays[0][0], arrays[0][-1]
        ans = 0
        for arr in arrays[1:]:
            ans = max(ans, abs(low - arr[-1]), abs(high - arr[0]))
            low = min(low, arr[0])
            high = max(high, arr[-1])
        return ans

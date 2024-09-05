from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mSum = sum(rolls)
        x = mean * (m + n) - mSum

        if not (n <= x <= 6 * n):
            return []

        result = [1] * n
        remaining = x - n

        for i in range(n):
            increment = min(remaining, 5)
            result[i] += increment
            remaining -= increment

            if remaining == 0:
                break

        return result

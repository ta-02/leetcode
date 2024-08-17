from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R = len(points)
        C = len(points[0])

        dp = [0] * C

        for r in range(R):
            temp = [-1] * C

            left = [-1] * C
            for i in range(C):
                num = max(dp[i], left[i - 1] - 1 if i > 0 else dp[i])
                left[i] = num

            right = [-1] * C
            for i in range(C - 1, -1, -1):
                num = max(dp[i], right[i + 1] - 1 if i < C - 1 else dp[i])
                right[i] = num

            for c in range(C):
                temp[c] = points[r][c] + max(left[c], right[c])

            dp = temp

        return max(dp)

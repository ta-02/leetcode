from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MAX = 24 * 60
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)

        minutes.sort()

        res = MAX
        n = len(minutes)

        for i in range(n):
            curr = minutes[i]
            next = minutes[(i + 1) % n]
            diff = (next - curr) % MAX
            res = min(res, diff)

        return res
